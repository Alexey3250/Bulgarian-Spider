# Project: Web Scraping, Text Processing, and Question Answering

This project demonstrates the following tasks:

1. Web scraping to extract comments from a website.
2. Saving the extracted comments in a text file and a PDF file.
3. Reading text from a text file and splitting it into smaller chunks for further processing.
4. Using OpenAI's DocumentSearch to find relevant documents for a given query.
5. Answering the query based on the relevant documents using OpenAI's Question-Answering chain.

## Task 1: Web Scraping

The Python script uses the `requests` and `BeautifulSoup` libraries to scrape comments from a website. The comments are extracted, and their author, timestamp, and message are stored in a list of dictionaries.

## Task 2: Saving Comments in Text and PDF Files

The extracted comments are saved in a text file (`comments.txt`) using the built-in `open` function in Python. Additionally, the comments are saved in a PDF file (`comments.pdf`) using the `fpdf` library.

## Task 3: Reading and Splitting Text

The text is read from a file (`comments.txt`) and split into smaller chunks using the `CharacterTextSplitter` from OpenAI's DocumentSearch. The splitting helps avoid token size limits during information retrieval.

## Task 4: Finding Relevant Documents

The OpenAI's DocumentSearch is used to create a FAISS index for efficient similarity searching. A query is provided, and the script finds the most similar documents (text chunks) from the `texts` variable.

## Task 5: Question Answering

The OpenAI's Question-Answering chain is used to generate an answer based on the information in the relevant documents. The query and the relevant documents are used as input, and the answer is returned as output.

## Dependencies

To run the code, the following libraries need to be installed:

- requests
- beautifulsoup4
- fpdf
- openai
- faiss-cpu

You can install them using the following command:

```bash
pip install requests beautifulsoup4 fpdf openai faiss-cpu
