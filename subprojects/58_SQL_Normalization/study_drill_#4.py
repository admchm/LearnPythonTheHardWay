## Study Drill #4
## SELECT count(*) as total, currency.currency
##   FROM rate, currency
##   WHERE rate.currency_id = currency.id
##   AND rate.rate is null
##   GROUP BY currency.currency
##   ORDER BY total DESC;
## 

# Answer: ---