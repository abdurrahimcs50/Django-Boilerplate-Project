# Django Boilerplate Project

This is a boilerplate project for Django applications. It includes Python, Django, PostgreSQL, Docker, Celery, and Redis.

## Table of Contents
- [Django Boilerplate Project](#django-boilerplate-project)
  - [Table of Contents](#table-of-contents)
  - [Getting Up and Running Locally](#getting-up-and-running-locally)
    - [Requirements](#requirements)
    - [Setting Up Development Environment with Python](#setting-up-development-environment-with-python)
    - [Now, you can visit http://localhost:8000 in your web browser to see your application.](#now-you-can-visit-httplocalhost8000-in-your-web-browser-to-see-your-application)
- [Build the Stack On Local and Production Development Using Docker and Docker Compose.](#build-the-stack-on-local-and-production-development-using-docker-and-docker-compose)
  - [Execute Management Commands](#execute-management-commands)
    - [For production:](#for-production)
  - [License](#license)
  - [Contributing](#contributing)
  - [Ways to Contribute](#ways-to-contribute)
  - [Acknowledgments](#acknowledgments)
  - [Contact](#contact)

## Getting Up and Running Locally

### Requirements

Make sure to have the following on your host:

- Python
- Django
- Postgres
- Celery
- Redis

### Setting Up Development Environment with Python

1. **Clone the repository**: Clone this repository to your local machine.

    ```bash
    git clone https://github.com/abdurrahimcs50/Django-Boilerplate-Project.git
    ```

2. **Set up a virtual environment**: It’s a good practice to create a virtual environment for your project to isolate your project’s dependencies.

    ```bash
    # Create a virtualenv:
    python -m venv venv
    # Activate the virtualenv you have just created:
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install development requirements**: Install the project dependencies from the requirements.txt file.

    ```bash
    cd Django-Boilerplate-Project
    pip install -r requirements.txt
    ```

4. **Set up environment variables**: Copy the .env.example file to a new file called .env, and fill in your actual values.

    ```bash
    cp .env.example .env

    # Example .env

    SECRET_KEY=changeme
    ALLOWED_HOSTS=localhost 127.0.0.1
    DEBUG=1
    CSRF_TRUSTED_ORIGINS=https://*.example.com https://*.192.162.0.0.1

    ENGINE=django.db.backends.postgresql
    POSTGRES_DB=changeme
    POSTGRES_PASSWORD=changeme
    POSTGRES_USER=changeme
    POSTGRES_HOST=changeme
    POSTGRES_PORT=changeme
    ```

5. **Run migrations**: Django uses a database-abstraction API that lets you create, retrieve, update, and delete records.

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Start the server**: You can start the server using the Django’s built-in server for development.

    ```bash
    python manage.py runserver
    ```

### Now, you can visit http://localhost:8000 in your web browser to see your application.

# Build the Stack On Local and Production Development Using Docker and Docker Compose.

1. **Build the Docker images:**
    ```bash
    docker-compose -f local_dev.yml build
    ```

    For production:
    ```bash
    docker-compose -f production.yml build
    ```

2. **Run the Docker containers:**
    ```bash
    docker-compose -f local_dev.yml up

    # For detached (background) mode, use:
    docker-compose -f local_dev.yml up -d
    ```

    For production:
    ```bash
    docker-compose -f production.yml up

    # For detached (background) mode, use:
    docker-compose -f production.yml up -d
    ```

    Visit http://localhost:8000 in your web browser for local development or http://localhost or http://127.0.0.1 for production.

3. ### Important Note:
    - In the context of executing commands, the term `web` refers to the target service. Please be aware that using `docker exec` is not suitable for running management commands in this scenario.

## Execute Management Commands

```bash
# Use the following commands to manage your Django application within the Docker container:

# For local development:
docker-compose -f local_dev.yml run --rm web python manage.py makemigrations
docker-compose -f local_dev.yml run --rm web python manage.py migrate
docker-compose -f local_dev.yml run --rm web python manage.py collectstatic
docker-compose -f local_dev.yml run --rm web python manage.py createsuperuser
docker-compose -f local_dev.yml run --rm web python manage.py startapp app_name
docker-compose -f local_dev.yml run --rm web python manage.py shell

# For production:
docker-compose -f production.yml run --rm web python manage.py makemigrations
docker-compose -f production.yml run --rm web python manage.py migrate
docker-compose -f production.yml run --rm web python manage.py collectstatic
docker-compose -f production.yml run --rm web python manage.py createsuperuser
docker-compose -f production.yml run --rm web python manage.py startapp app_name
docker-compose -f production.yml run --rm web python manage.py shell

## Running Tests

To run the tests for your Django application, you can use the following command within the Docker container:

### For local development:

```bash
docker-compose -f local_dev.yml run --rm web python manage.py test
```

### For production:

```bash
docker-compose -f production.yml run --rm web python manage.py test

```

This command will execute all the tests in your project, providing feedback on the success or failure of each test case.

**Note:** It's recommended to write tests for your Django application to ensure its stability and reliability. You can create test files in the `tests` directory of your Django app or follow [Django's testing documentation](https://docs.djangoproject.com/en/stable/topics/testing/) for more information: Django Testing Documentation.

## License

This project is licensed under the MIT License.

## Contributing

👏 Contributions are welcome! Whether you're reporting bugs, suggesting enhancements, or contributing code, your efforts are appreciated.

## Ways to Contribute

1. **Reporting Bugs**: If you encounter issues or unexpected behavior, please create a new issue. Be sure to provide detailed information about the problem and steps to reproduce it.

2. **Suggesting Enhancements**: Have an idea for improvement? Feel free to suggest it by creating an issue and describing your enhancement.

3. **Code Contributions**: Want to contribute code? Check the existing issues and pull requests to avoid duplication. Make your changes, test them locally, and submit a pull request.

4. **Writing Documentation**: If you find something that needs better documentation or want to contribute to our docs, that's fantastic! Clear documentation helps everyone understand and use the project effectively.

5. **Providing Feedback**: Share your experiences, suggestions, or concerns. Your feedback helps us make the project better.

6. **Sharing the Project**: If you find this project useful, consider sharing it with others. Spread the word on social media, tech communities, or among your colleagues. The more, the merrier.

## Acknowledgments

Special thanks to the Python, Django, PostgreSQL, Docker, Celery, and Redis communities for their invaluable contributions.

## Contact

For inquiries, please contact [admin@rahim.com.bd](mailto:admin@rahim.com.bd) or visit [https://www.rahim.com.bd](https://www.rahim.com.bd).


