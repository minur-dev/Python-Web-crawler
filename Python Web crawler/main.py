import requests
from bs4 import BeautifulSoup

def get_links(url):
    # Make a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    # Find all the <a> tags on the page
    links = soup.find_all("a")
    # Extract the href attribute from each <a> tag
    hrefs = [link.get("href") for link in links]
    # Return the list of links
    return hrefs

# Example usage
links = get_links("https://www.iana.org/domains/example")
print(links)
