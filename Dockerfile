# Use the official Python image as the base image
FROM python:3.12.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install PostgreSQL libraries and headers (needed for psycopg2)
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app (app.py) into the container
COPY app.py .

# Expose the port that Streamlit uses (default is 8501)
EXPOSE 8501

# Command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]