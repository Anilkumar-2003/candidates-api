# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy app files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
