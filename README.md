# Django Test Sentry Logs

This project demonstrates logging at different levels (debug, info, warning) in a Django application and integrates with Sentry for error reporting.

## Setup Instructions

### 1. Create the Environment

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd test-sentry-logs-django
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Configure Environment Variables

1. Copy the `.env.sample` file to `.env`:
   ```bash
   cp .env.sample .env
   ```

2. Open the `.env` file and update the `SENTRY_DSN` key with your actual Sentry DSN:
   ```env
   SENTRY_DSN=<your-sentry-dsn>
   ```

### 3. Run the Django Application

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

### 4. Test the Logging View

You can test the logging functionality by sending a GET request to the `/logs/logger_test/` endpoint:

```bash
curl http://127.0.0.1:8000/logs/logger_test/
```

This will generate logs at different levels (debug, info, warning) and return a JSON response:

```json
{
  "message": "Logs generated"
}
```
