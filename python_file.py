import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Function to scrape a random Wikipedia article
def get_wiki_data():
    url = "https://www.geeksforgeeks.org/python-programming-language"
    url_data = requests.get(url)
    if url_data.status_code == 200:
        return url_data.text
    else:
        return None

# Function to extract text content from HTML
def get_text_from_html(html):
    text_data = BeautifulSoup(html, 'html.parser')
    paragraphs = text_data.find_all('p')
    text_output = ' '.join([p.get_text() for p in paragraphs])
    print('text output:',text_output)
    return text_output

# Function to clean and process text
def text_modification(text):
    text = re.sub(r'\W+', ' ', text)  # Remove non-alphanumeric characters
    text = text.lower()  # Convert text to lowercase
    return text

# Function to calculate top 5 most frequent words
def calculate_common_words(text):
    words = text.split()
    word_count = Counter(words)
    common_words = word_count.most_common(5)
    return common_words

# Function to write text to a file
def write_to_text_file(text):
    with open('wikipedia_article.txt', 'w', encoding='utf-8') as file:
        file.write(text)

# Scrape a random Wikipedia article
html_content = get_wiki_data()
if html_content:
    # Extract text content
    text_content = get_text_from_html(html_content)

    # Process text
    processed_text = text_modification(text_content)

    # Write processed text to a file
    write_to_text_file(processed_text)

    # Calculate top 5 most frequent words
    top_5_words = calculate_common_words(processed_text)

    # Display top 5 most frequent words
    print("Top 5 most frequent words:")
    for word, count in top_5_words:
        print(f"{word}: {count}")
else:
    print("Failed to fetch Wikipedia article.")
