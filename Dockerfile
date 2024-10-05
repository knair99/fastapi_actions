# Use official Python 3.12 image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files to the container
COPY . .

# Install Poetry and project dependencies
RUN pip install poetry
RUN poetry install --no-interaction --no-ansi  # Install all dependencies, including dev

# Expose the FastAPI port
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
