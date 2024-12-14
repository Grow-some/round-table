# Use the official Python image from the Docker Hub
FROM python:3.13-bookworm

# Set the working directory in the container
WORKDIR /app

# Install OS-level dependencies if required
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port your Flask application runs on
EXPOSE 5000

# Command to run your Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
