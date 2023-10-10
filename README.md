# Django REST Framework (DRF) Recipe APP API Template

This is a template for building a Python Django REST Framework (DRF) project with best practices, including Test-Driven Development (TDD), and Docker setup for easy development and deployment.

## Getting Started

Follow these steps to set up and run the project locally using Docker:

### Prerequisites

1. [Docker](https://www.docker.com/get-started) installed on your system.

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Rokuflam/recipe-app-api.git
cd recipe-app-api
```


### Environment Variables

Create a **`.env`** file in the project root and configure the following environment variables:

```dotenv
DB_NAME=dbname
DB_USER=rootuser
DB_PASS=changeme
DJANGO_SECRET_KEY=changeme
DJANGO_ALLOWED_HOSTS=127.0.0.1
```

Replace **`changeme`**, **`rootuser`**, and **`dbname`** with your own values.


### Build and Run with Docker

Build the Docker containers and start the project:

```bash
docker-compose build
docker-compose up
```

This will launch the Django development server and PostgreSQL database in Docker containers.

### Run Migrations
In a separate terminal, run database migrations:

```bash
docker-compose run --rm app sh -c "python manage.py migrate"
```
### Run Tests
To run the tests using TDD:

```bash
docker-compose run --rm app sh -c "python manage.py test && flake8"
```

### Access the OpenAI API
The API will be available at http://localhost:8000/api/docs/.

### Project Structure

The project structure follows best practices:

- `proxy/`: Configuration settings for Nginx.
- `scripts/`: Configuration settings for running app on the host.
- `app/app/`: Django app with main settings.
- `app/core/`: Django app for models.
- `app/user/`: Django app for user auth.
- `app/recipe/`: Django app for recipe API.
- `app/*/tests/`: Unit tests for the app using TDD.
- `Dockerfile`: Docker configuration for the project.
- `docker-compose.yml`: Docker Compose configuration for development.
- `requirements.txt`: Python dependencies for the project.
- `README.md`: This documentation.

### Contributing

Feel free to contribute to this project by opening issues or pull requests. Follow the [Contributing Guidelines](CONTRIBUTING.md) for more details.

### License

Here no License, so feel free to use it.

### Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
