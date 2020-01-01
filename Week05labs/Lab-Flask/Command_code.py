curl -i http://localhost:5000/cars

curl -i http://localhost:5000/cars/test

curl -i -H "Content-Type:application/json" -X POST -d '{"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars

curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234

curl -i -X DELETE http://localhost:5000/cars/181%20G%201234