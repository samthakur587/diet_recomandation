# Use an official Python runtime as the base image
FROM python:3.9 

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirement.txt /app/

RUN  pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the application's code into the container at /app
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
