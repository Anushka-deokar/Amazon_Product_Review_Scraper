# Import the necessary libraries
from bs4 import BeautifulSoup as bs  # BeautifulSoup is used for parsing HTML content
import requests  # Requests is used to send HTTP requests

# URL of the Amazon product page you want to scrape
link = "https://www.amazon.in/Vendoz-Women-Stylish-Casual-Sneakers/dp/B0B5VFLR68/ref=asc_df_B0B5VFLR68/?tag=googleshopdes-21&linkCode=df0&hvadid=610186779037&hvpos=&hvnetw=g&hvrand=16512439340853383867&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007780&hvtargid=pla-1696229204540&psc=1&mcid=7223dd89be8b3025a76a510c23bc993d"

# Send an HTTP GET request to the Amazon product page
page = requests.get(link)

# Check the HTTP response status
# Response 503 means service unavailable, Response 200 means the page was successfully fetched
print("Response status:", page)

# Get the raw HTML content of the page
raw_html = page.content

# Parsing the HTML using BeautifulSoup with the 'html.parser'
soup = bs(raw_html, 'html.parser')

# Print the raw HTML in a structured (pretty) format for better readability
print("Formatted HTML:")
print(soup.prettify())

# Display the list of immediate child elements in the parsed HTML
print("Children of the parsed HTML:")
print(list(soup.children))

# Try to find specific data (e.g., product reviews section)
# The HTML structure of the product reviews section is identified by the class name
# Note: This class name might need to be adjusted based on the actual HTML structure of Amazon pages
title = soup.find_all('div', class_="a-section a-spacing-none review-views celwidget.span")

# Output the result to see what was found
print("Extracted reviews section:")
print(title)
