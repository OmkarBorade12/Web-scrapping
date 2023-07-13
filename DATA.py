# Import the libraries useful for scraping
import csv
import requests
from bs4 import BeautifulSoup

# Function to scrape data from the table and store in a CSV file
def scrape_tea():
    base_url = "https://www.teaboard.gov.in/WEEKLYPRICES/"

    # Open CSV file for writing
    with open('average_d.csv', 'w', newline='') as csvfile:
        fieldnames = ['week', 'location', 'average_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate over years from 2008 to 2023
        for year in range(2008, 2024):
            url = f"{base_url}{year}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the table with id
            table = soup.find('table', id='contn_GridView2')
            # Find all rows in the table (excluding header row)
            rows = table.find_all('tr')[1:]

            # Iterate over rows and extract data
            for row in rows:
                cells = row.find_all('td')
                week = cells[0].text.strip()
                location = cells[1].text.strip()
                average_price = cells[2].text.strip()

                # Write data to CSV file
                writer.writerow({'week': week, 'location': location, 'average_price': average_price})

# Call the function to start scraping
scrape_tea()
