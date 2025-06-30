# Use official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install flask flask-cors

# Expose the port used by Flask
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
# Use a non-root user to run the application
RUN adduser --disabled-password --gecos '' appuser
USER appuser