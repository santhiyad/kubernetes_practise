# Ubuntu OS
FROM ubuntu

# installation
RUN apt-get update
RUN apt-get install -y python3 python3-pip

# Change work directory to /opt 
WORKDIR /app

# Copy the code into the container at /opt location
COPY . . 

# Installation
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port-5000 
EXPOSE 5000

CMD ["python3","app.py"]

