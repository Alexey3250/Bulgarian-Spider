import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Replace this with the URL of your forum thread
url = "https://bglife.ru/topic/978/"

# Fetch the HTML content of the forum thread
response = requests.get(url)
html_content = response.text

# Parse the HTML content and extract the relevant thread data
soup = BeautifulSoup(html_content, "html.parser")
posts = soup.find_all(class_="post")  # Adjust the class or tag based on the forum structure

# Create a new PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add content to the PDF document
for post in posts:
    author = post.find(class_="author")  # Adjust the class or tag based on the forum structure
    content = post.find(class_="content")  # Adjust the class or tag based on the forum structure
    
    # Add a new page for each post
    pdf.add_page()

    # Set font for author and content
    pdf.set_font("Arial", size=12)
    
    # Write author information
    if author:
        pdf.cell(0, 10, author.text.strip(), ln=True)

    # Write post content
    if content:
        pdf.multi_cell(0, 10, content.text.strip())

# Save the PDF document to a local file
pdf.output("forum_thread.pdf")
