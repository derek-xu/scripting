import requests
from bs4 import BeautifulSoup

def scrape_cnn_headlines():
    url = "https://www.cnn.com/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # CNN often places headlines in <h3> tags with classes such as 'cd__headline'
    # Example: <h3 class="cd__headline"><a href="/2025/01/19/us/some-story">Headline text</a></h3>
    headlines = soup.find_all("h3", class_="cd__headline")
    
    results = []
    for h in headlines:
        # Headline text might be inside an <a> tag
        a_tag = h.find("a")
        if a_tag:
            title = a_tag.get_text(strip=True)
            link = a_tag.get("href")
            
            # Some links might be relative (e.g., "/us/article"), prepend CNN domain if needed
            if link.startswith("/"):
                link = f"https://www.cnn.com{link}"
            
            results.append({
                "title": title,
                "link": link
            })
    
    # Print or return your collected headlines
    for item in results:
        print(f"{item['title']} -> {item['link']}")
    
    return results


if __name__ == "__main__":
    headlines_data = scrape_cnn_headlines()

