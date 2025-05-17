# Random Password Generator

A Django-based web application that generates secure random passwords with customizable options.

## Features

- Generate passwords of custom length
- Option to include brackets
- Option to include special characters
- Simple and clean interface

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd random-password-generator
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
# Create a .env file in the project root
cp .env.example .env  # If you have an example file
# Or create .env manually with these variables:
DJANGO_SECRET_KEY='your-secret-key-here'
DEBUG=True
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to use the application.

## Security

This application implements several security measures:

- Content Security Policy (CSP)
- XSS Protection
- CSRF Protection
- HSTS
- Secure Cookie Settings
- Environment-based configuration
- No sensitive data in version control

## License

MIT License
