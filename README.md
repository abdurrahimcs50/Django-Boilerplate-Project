# Django-Boilerplate-Project

This is a boilerplate project for Django applications. It includes Django, PostgreSQL, Docker, Celery, Redis, ElasticSearch, and Rabbitmq.

## Getting Up and Running Locally

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Make sure to have the following on your host:

- Python
- Django
- Postgres
- Celery
- Redis
- ElasticSearch

### Setting Up Development Environment with python: 

1. **Clone the repository**: Clone this repository to your local machine.

```bash
git clone https://github.com/abdurrahimcs50/Django-Boilerplate-Project.git
```
2. **Set up a virtual environment**: It’s a good practice to create a virtual environment for your project to isolate your project’s dependencies.
   
```bash
#Create a virtualenv:
python -m venv <virtual env path>
python -m venv venv
#Activate the virtualenv you have just created:
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```
3. **Install development requirements**: Install the project dependencies from the requirements.txt file.

```python
cd <path requirements.txt>

pip install -r requirements.txt

```
4. **Set up environment variables**: Copy the .env.example file to a new file called .env, and fill in your actual values.

```bash
cp .env.example .env

# example .env

SECRET_KEY=changeme
ALLOWED_HOSTS=localhost 127.0.0.1
DEBUG=1
CSRF_TRUSTED_ORIGINS=https://*.example.com https://*.192.162.0.0.1

ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

```
5. **Run migrations**: Django uses a database-abstraction API that lets you create, retrieve, update, and delete records.

```python

python manage.py makemigrations
python manage.py migrate

```
6. **Start the server**: You can start the server using the Django’s built-in server for development.
   
```python

python manage.py runserver
```
### Now, you can visit http://localhost:8000 in your web browser to see your application.

# Getting Up and Running Locally With Docker.

### Make sure to have the following on your host:
- Docker
- Docker Compose

```bash
# example dev.env for local_dev.yml
SECRET_KEY=changeme
ALLOWED_HOSTS=localhost 127.0.0.1
DEBUG=1
CSRF_TRUSTED_ORIGINS=https://*.example.com https://*.192.162.0.0.1

ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

```
  
### Build the Stack
1. **Build the Docker images: Docker Compose builds everything your application needs to run. Use the following command to build your Docker images:**
```bash
docker-compose -f local_dev.yml build

```
2. **Run the Docker containers: After building the images, you can run your application with the following command:**
   
```bash
docker-compose -f local_dev.yml up

# To run in a detached (background) mode, just:
docker-compose -f local_dev.yml up -d

```
## Now, your Django application should be running at localhost:8000. You can visit http://localhost:8000 in your web browser to see your application.

# Execute Management Commands

```bash
# As with any shell command that we wish to run in our container, this is done using the docker compose -f local_dev.yml run --rm command:

# Create database migrations:
docker compose -f local_dev.yml run --rm web python manage.py makemigrations

# Apply database migrations:
docker compose -f local_dev.yml run --rm web python manage.py migrate

# Collect static files:
docker compose -f local_dev.yml run --rm web python manage.py collectstatic

# Create a Django superuser:
docker compose -f local_dev.yml run --rm web python manage.py createsuperuser

# Create A New Django App:
docker compose -f local_dev.yml run --rm web python manage.py startapp app_name

# Access the Django shell:
docker compose -f local_dev.yml run --rm web python manage.py shell

```

# OR

```bash
# Access bash in the Docker container: If you want to access the bash shell in the Docker container, you can use the exec command with Docker Compose:

docker-compose -f local_dev.yml exec web sh

# Run the Django development server:
docker-compose -f local_dev.yml exec web python manage.py runserver

# Create database migrations:
docker-compose -f local_dev.yml exec web python manage.py makemigrations

# Apply database migrations:
docker-compose -f local_dev.yml exec web python manage.py migrate

# Create A New Django App:
docker-compose -f local_dev.yml exec web python manage.py startapp app_name

# Create a Django superuser:
docker-compose -f local_dev.yml exec web python manage.py createsuperuser

# Collect static files:
docker-compose -f local_dev.yml exec web python manage.py collectstatic

# Access the Django shell:
docker-compose -f local_dev.yml exec web python manage.py shell

# Check for problems in your project without making migrations or touching the database:
docker-compose -f local_dev.yml exec web python manage.py check

```

### ### Here, web is the target service we are executing the commands against. Also, please note that the docker exec does not work for running management commands.


### Setting Up for Production Environment:

```bash

# example prod.env for production.yml
SECRET_KEY=changeme
ALLOWED_HOSTS=localhost 127.0.0.1
DEBUG=0
CSRF_TRUSTED_ORIGINS=https://*.example.com https://*.192.162.0.0.1

ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

```

### Build the Stack
1. **Build the Docker images: Docker Compose builds everything your application needs to run. Use the following command to build your Docker images:**
```bash
docker-compose -f production.yml build

```
2. **Run the Docker containers: After building the images, you can run your application with the following command:**
   
```bash
docker-compose -f production.yml up

# To run in a detached (background) mode, just:
docker-compose -f production.yml up -d

```
## Now, your Django application should be running at localhost:8000. You can visit http://localhost or http://127.0.0.1 in your web browser to see your application.

# Execute Management Commands

```bash
# As with any shell command that we wish to run in our container, this is done using the docker compose -f local_dev.yml run --rm command:

# Create database migrations:
docker compose -f production.yml run --rm web python manage.py makemigrations

# Apply database migrations:
docker compose -f production.yml run --rm web python manage.py migrate

# Collect static files:
docker compose -f production.yml run --rm web python manage.py collectstatic

# Create a Django superuser:
docker compose -f local_dev.yml run --rm web python manage.py createsuperuser

# Create A New Django App:
docker compose -f production.yml run --rm web python manage.py startapp app_name

# Access the Django shell:
docker compose -f production.yml run --rm web python manage.py shell

```

# OR

```bash
# Access bash in the Docker container: If you want to access the bash shell in the Docker container, you can use the exec command with Docker Compose:

docker-compose -f production.yml exec web sh

# Run the Django development server:
docker-compose -f production.yml exec web python manage.py runserver

# Create database migrations:
docker-compose -f production.yml exec web python manage.py makemigrations

# Apply database migrations:
docker-compose -f production.yml exec web python manage.py migrate

# Create A New Django App:
docker-compose -f production.yml exec web python manage.py startapp app_name

# Create a Django superuser:
docker-compose -f production.yml exec web python manage.py createsuperuser

# Collect static files:
docker-compose -f production.yml exec web python manage.py collectstatic

# Access the Django shell:
docker-compose -f production.yml exec web python manage.py shell

# Check for problems in your project without making migrations or touching the database:
docker-compose -f production.yml exec web python manage.py check

```

### ### Here, web is the target service we are executing the commands against. Also, please note that the docker exec does not work for running management commands.
