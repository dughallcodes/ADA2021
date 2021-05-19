echo "Let's get this bread"
docker-compose up -d --b rabbitmq
wait
echo "🥱 Waiting for rabbitMQ to start"
sleep 15s
docker-compose up -d --b
echo "😪 Creating users database"
docker-compose exec users python manage.py migrate
wait
echo "🥱 Creating orders database"
docker-compose exec orders python manage.py migrate
wait
docker-compose exec orders_consumer python manage.py migrate
wait
echo "😴 Creating couriers database"
docker-compose exec couriers python manage.py migrate
echo "😎 Done!"