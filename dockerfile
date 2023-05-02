# Use the official manim community image as the base image
FROM manimcommunity/manim:latest

# Set the working directory to /app
WORKDIR /app

USER root

# Copy the source code from the current directory to /app in the container
COPY ./src /app
RUN chmod +x -R /app

# Define an environment variable to set the PYTHONPATH to include /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Define an entrypoint command to run your code with arguments
ENTRYPOINT ["python", "/app/manimcs.py"]

# Expose the /app/output directory as a volume
VOLUME ["/app/output"]
