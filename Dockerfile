# Step 1: Use an official Python base image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED=1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . /app/

# Step 6: Expose the port the app will run on
EXPOSE 5000

# Step 7: Define the command to run the application
CMD ["python", "app.py"]
