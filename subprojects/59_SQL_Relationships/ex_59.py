# One-to-Many in Python

# class Rate:
#   def __init__(self, date, rate, currency):
#     self.date = date
#     self.rate = rate
#     self.currency = currency

# class Currency:
#   def __init__(self, rates):
#     # rates is a list but...wait
#     self.rates = rates

# One-to-Many Problem
# jan_usd = [Rate('Jan', 1.2, usd), Rate('Jan', 1.3, usd)]
# usd = Currency(jan_usd)

# Querying M:M Tables
# SELECT count(*) FROM
#   rate, currency, rate_currency
#   WHERE rate.id=rate_currency.rate_id
#   AND currency.id=rate_currency.currency_id
#   AND currency.currency='USD'
#   AND date(rate.date) > date('2023-01-01');


# SELECT count(*) FROM rate
#   JOIN currency
#     ON rate_currency.currency_id=currency.id
#   JOIN rate_currency
#     ON rate_currency.rate_id=rate.id
#   WHERE currency.currency='USD'
#   AND date(rate.date) > date('2023-01-01');