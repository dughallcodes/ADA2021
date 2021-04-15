ALTER USER postgres WITH PASSWORD 'postgres';
SELECT 'CREATE DATABASE users'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'users')\gexec