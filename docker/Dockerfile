FROM puckel/docker-airflow:1.10.1

USER root

# Install Git
RUN apt-get update && \
    apt-get install -y git

# Copy and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

USER airflow

