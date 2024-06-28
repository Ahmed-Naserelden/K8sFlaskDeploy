FROM python

# Set the working directory
WORKDIR /app

# Copy the application files to the working directory
COPY app.py .

# Install Flask
RUN pip install Flask

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD [ "python3", "app.py"]
