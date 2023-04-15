import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        self.url = 'https://bank.gov.ua/ua/markets/exchangerates'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.exchange_rates = self.soup.find('table', class_='exchange-rates-table')

    def get_usd_rate(self):
        usd_row = self.exchange_rates.find('tr', {'data-currency': 'USD'})
        usd_rate = float(usd_row.find('td', class_='td-rate').text)
        return usd_rate

    def convert(self, amount):
        usd_rate = self.get_usd_rate()
        usd_amount = amount / usd_rate
        return round(usd_amount, 2)


if __name__ == '__main__':
    converter = CurrencyConverter()
    uah_amount = float(input("Enter amount in UAH: "))
    usd_amount = converter.convert(uah_amount)
    print("{} UAH is equal to {} USD".format(uah_amount, usd_amount))
