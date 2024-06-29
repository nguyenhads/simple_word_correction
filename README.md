# Word Correction Using Levenshtein Distance

This project uses Levenshtein distance to correct words by comparing them against a vocabulary list. The application is built with Streamlit, a Python library for creating web apps.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Introduction

Levenshtein distance, also known as edit distance, is a metric for measuring the difference between two strings. It calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into another. This project utilizes Levenshtein distance to find the closest matching word from a predefined vocabulary list.

## Installation

To run this project, you need to have Python installed. Follow these steps to set up and run the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/nguyenhads/simple_word_correction.git
   cd simple_word_correction
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your vocabulary file. Create a file named `vocab.txt` inside a `data` directory. This file should contain a list of words, each on a new line.

2. Run the Streamlit application:

   ```bash
   streamlit run levenshtein_distance.py
   ```

3. Open your web browser and go to the provided URL (usually `http://localhost:8501`).

4. Input a word in the text box and click the "Compute" button to find the closest matching word from the vocabulary list.

## File Structure

```
simple_word_correction/
├── data/
│ └── vocab.txt
├── levenshtein_distance.py
├── requirements.txt
└── README.md

```

- `data/vocab.txt`: Contains the vocabulary list.
- `levenshtein_distance.py`: The main application script.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: Project documentation.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- Streamlit: https://streamlit.io/
- Levenshtein distance: https://en.wikipedia.org/wiki/Levenshtein_distance
