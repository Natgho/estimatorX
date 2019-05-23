# Estimator-X
Arima veya prophet öğrenme modellerini kullanarak veri tahmininde bulunun program.




## Teknik Kurulum
Redis ve postgresql için containerlar;
```
docker run --name rd -p  7001:6379 -d redis
docker run -d -p 5432:5432 --name ps -e POSTGRES_PASSWORD=postgres postgres
sudo apt-get install libpq-dev python-dev
```