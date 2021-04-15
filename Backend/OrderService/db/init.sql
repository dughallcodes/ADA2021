ALTER USER postgres WITH PASSWORD 'postgres';
SELECT 'CREATE DATABASE orders'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'orders')\gexec