# Flipkart Product Web Scraping
This project is a Python-based web scraping tool that allows you to extract product data from Flipkart, one of the leading e-commerce websites. It utilizes the power of Python libraries such as BeautifulSoup and Requests to scrape product details like product name, customer name, ratings, and comments from Flipkart's web pages.

### Table of Contents
- Installation
- Usage
- Features
- Contributing

## Installation
To use this project, follow the steps below:

### 1.Clone the repository to your local machine:
https://github.com/sanjanashinde416502/Web-Scrapping-Project-on-21st-Feb-2023.git

### 2.Navigate to the project directory:
cd review-scrapper-aws-main

### 3.Install the required dependencies:
pip install -r requirements.txt

### 4.You're all set! Now you can start using the Flipkart Product Web Scraping tool.

## Usage
To scrape product data from Flipkart, you need to provide the URL of the Flipkart product page you want to scrape. Modify the url variable in the main.py file with the desired URL.
url = "https://www.flipkart.com/some-product-page"

After modifying the URL, run the main.py file:
python app.py

The script will fetch the product details and save them to a CSV file named products.csv.

## Features
- Scrapes product details such as product name, customer name, ratings, and comments from Flipkart.
- Supports scraping multiple pages by automatically navigating through pagination.
- Saves the scraped data to a CSV file for further analysis or usage.
  
## Contributing
Contributions are welcome! If you find any issues or want to enhance the functionality of this project, please submit a pull request. Additionally, if you encounter any bugs or have suggestions for improvement, please open an issue.
