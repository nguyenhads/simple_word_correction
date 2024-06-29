import streamlit as st


def load_vocab(file_path):
    """Load vocabulary from file_path"""

    with open(file_path, "r") as f:
        lines = f.readlines()

    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def levelshtein_distance(token1, token2):
    """Calculate levelshtein distance between 2 tokens"""

    dp = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    for i in range(len(token1) + 1):
        dp[i][0] = i

    for j in range(len(token2) + 1):
        dp[0][j] = j

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 1,
                )

    return dp[len(token1)][len(token2)]


def main():
    st.title("Word Correction Using Levenshtein Distance")
    word = st.text_input("Input your word:")
    vocabs = load_vocab(file_path="./data/vocab.txt")

    if st.button("Compute"):
        leven_dis = dict()
        for vocab in vocabs:
            leven_dis[vocab] = levelshtein_distance(word, vocab)

        # Sorted by distance
        sorted_dis = dict(sorted(leven_dis.items(), key=lambda item: item[1]))
        correct_word = list(sorted_dis.keys())[0]
        st.write("Corrected word:", correct_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary:")
        col1.write(vocabs)

        col2.write("Distance:")
        col2.write(sorted_dis)


if __name__ == "__main__":
    #     words = load_vocab(file_path="./data/vocab.txt")
    #     # print(words)

    #     token1 = "bok"
    #     for token2 in words:
    #         print(
    #             f"Levenshtein distance giữa '{token1}' và '{token2}' là {levelshtein_distance(token1, token2)}"
    #         )
    main()
