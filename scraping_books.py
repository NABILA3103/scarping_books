import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

data = []

while url:
    print("Scraping:", url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").get_text(strip=True)
        rating = book.find("p", class_="star-rating")["class"][1]
        availability = book.find(
            "p", class_="instock availability"
        ).get_text(strip=True)

        data.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    # Mencari tombol halaman berikutnya
    next_page = soup.find("li", class_="next")

    if next_page:
        next_url = next_page.a["href"]

        if next_url.startswith("catalogue/"):
            url = "https://books.toscrape.com/" + next_url
        else:
            url = "https://books.toscrape.com/catalogue/" + next_url
    else:
        url = None

# Mengubah data menjadi DataFrame
df = pd.DataFrame(data)

# Menyimpan hasil scraping ke CSV
df.to_csv("books.csv", index=False)

print()
print("Scraping selesai!")
print("Jumlah buku:", len(df))
print("Data disimpan sebagai books.csv")
