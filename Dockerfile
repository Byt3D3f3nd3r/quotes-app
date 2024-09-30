# Use an official Python runtime as a base image
FROM python:3.9-slim

# Create working directory
WORKDIR /app-1

# Copy all the files to the working directory
COPY . /app-1

# Installs Flask 
RUN pip install Flask

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to allow access outside the container
EXPOSE 5000

# Debug: Print the installed packages
RUN pip freeze

# Command to run the Flask app and also enable debugging
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--debugger"]






