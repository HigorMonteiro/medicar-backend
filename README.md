# Step by step to run application:

### First step:
```
git git@github.com:HigorMonteiro/medicar-backend.git
cd medicar-backend/
mv env_sample.txt .env 
```
### Running with Docker:

1. [Install docker](https://docs.docker.com/install/)
2. [Install the docker-compose](https://docs.docker.com/compose/install/)

### Second step:
```
docker-compose build
docker-compose run web python manage.py migrate
docker-compose up
```
### access Admin at the address below:
url: http://localhost:8000

### access Api at the address below:
url: http://localhost:8000/api/

### Access Admin on heroku
url: https://medicar-backend.herokuapp.com/

email: demo@medicar.com.br
password: demo123