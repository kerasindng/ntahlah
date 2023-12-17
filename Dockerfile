# Use a more standard Python base image
FROM python:3.9.7-slim-buster

# Clone the repository
RUN git clone -b Userbothon https://github.com/kerasindng/ntahlah /home/Userbothon/ \
    && chmod -R 777 /home/Userbothon \
    && mkdir /home/Userbothon/bin/

# Set the working directory
WORKDIR /home/Userbothon/


# Set executable permission for start.sh
RUN chmod +x start.sh

# Expose any necessary ports if required
# EXPOSE 8080

# Specify the command to run on container start
CMD ["bash", "start.sh"]
