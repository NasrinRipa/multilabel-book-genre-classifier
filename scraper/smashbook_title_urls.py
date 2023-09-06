from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time

def extract_book_info(driver):
    try:
        # Find the container holding book information
        book_containers = driver.find_elements(By.CLASS_NAME, 'library-title')

        book_urls = []
        for container in book_containers:
            try:
                # Find the anchor element containing the book title and URL
                title = container.text
                book_url = container.get_attribute('href')
                book_urls.append({
                    "title": title,
                    "url": book_url
                })
                # Print the extracted title and URL
                print(f"Title: {title}\nURL: {book_url}\n")
            except Exception as e:
                print(f"Error extracting book data: {e}")

        return book_urls
    except Exception as e:
        print(f"Error extracting book containers: {e}")
        return []

if __name__ == "__main__":
    webdriver_path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path)
    base_url = "https://www.smashwords.com/books/category/{}/newest/0/any/any/"
    all_book_urls = []

    for category_num in tqdm(range(1000, 2001)):  # Loop through category numbers 1000 to 2000
        category_url = base_url.format(category_num)
        driver.get(category_url)
        # Wait for the page to load before searching for elements
        time.sleep(2)

        # Get book titles and URLs from the current category page
        category_book_urls = extract_book_info(driver)
        all_book_urls.extend(category_book_urls)

        # Check if there are multiple pages for the current category
        while True:
            try:
                next_page_btn = driver.find_element(By.LINK_TEXT, 'Next ›')
                next_page_btn.click()
                # Wait for the page to load before extracting data
                time.sleep(2)

                # Get book titles and URLs from the current page
                category_book_urls = extract_book_info(driver)
                all_book_urls.extend(category_book_urls)
            except Exception as e:
                break

    driver.quit()

    df = pd.DataFrame(data=all_book_urls, columns=["title", "url"])
    df.to_csv("smashbook_urls_2001.csv", index=False)
