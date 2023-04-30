FROM manimcommunity/manim:stable

# Set the working directory
WORKDIR /app
COPY . /app

# Copy the entrypoint script
#COPY entrypoint.sh /usr/local/bin/
#RUN chmod +x /usr/local/bin/entrypoint.sh

# Define the entrypoint command
#ENTRYPOINT ["entrypoint.sh"]

# Define the command to run when the container starts
#CMD ["manim", "-h"]