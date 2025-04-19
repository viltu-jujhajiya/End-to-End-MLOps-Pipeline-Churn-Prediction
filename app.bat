docker-compose build
docker-compose up -d

timeout /t 4

start http://localhost:1234