# MTECHAI-AIAC557
Certainly! Here's the markdown code with proper formatting so that you can easily copy it:

```markdown
## Sabji Spider - Web Scraping Tool

This repository contains a Python script that utilizes Scrapy to scrape vegetable prices from the "Kalimati Market" website and saves the data into a SQLite database. The script fetches the data for a specified date range and saves each entry in the `scraped_data` table of the SQLite database.

### Requirements

Make sure you have the following installed:

- Python
- Scrapy
- Pandas
- SQLite3

### Usage

1. Install the required dependencies:

```
pip install scrapy pandas
```

2. Clone the repository:

```
git clone https://github.com/kiranpantha/MTECHAI-AIAC557.git
cd sabjispider
```

3. Execute the spider:

```
scrapy crawl sabjispider
```

The spider will start scraping the vegetable prices and saving them to the `my_data.sqlite3` database.

### Code Explanation

The code defines a Scrapy spider named `SabjispiderSpider`. The spider fetches data from the "Kalimati Market" website and extracts vegetable prices for a given date range. The scraped data is then saved to a SQLite database.

The spider follows these steps:

1. Fetches the CSRF token required for form submission.
2. Iterates over the specified date range and submits a form request for each date to fetch the respective data.
3. Parses the response and extracts vegetable price details.
4. Creates a `SabjiItem` object for each vegetable entry and saves the data to the database.


### Database

The scraped data is stored in the `my_data.sqlite3` SQLite database. The database has a table named `scraped_data`, which contains the following columns:

- `date`: Date of the scraped data
- `name`: Name of the vegetable
- `weightUnit`: Unit of weight for the vegetable
- `minimumAmount`: Minimum price of the vegetable
- `maximumAmount`: Maximum price of the vegetable
- `averageAmount`: Average price of the vegetable

The `save_to_database` method is responsible for inserting the scraped data into the `scraped_data` table.

###Screenshot of DB "my_data.sqlite3"
![Image Description](https://raw.githubusercontent.com/kiranpantha/MTECHAI-AIAC557/main/db%20browser.png)
