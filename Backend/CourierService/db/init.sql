ALTER USER postgres WITH PASSWORD 'postgres';
SELECT 'CREATE DATABASE couriers'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'couriers')\gexec