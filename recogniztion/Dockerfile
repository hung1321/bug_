FROM centos:6

# Install necessary dependencies
RUN yum -y install epel-release
RUN yum -y install \ 
    tzdata \
    libopencv-devel \
    gcc-c++ \
    openssl-devel \
    postgresql-devel \
    libcurl-devel \
    expat-devel \
    git

# Switch back to non-root user
USER root
# Set up Python environment
FROM ubuntu:18.04
RUN sudo sed -i 's/https/http/g' /etc/yum.repos.d/epel.repo
RUN apt-get update && apt-get -y install \
    build-essential libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev wget

RUN wget http://nginx.org/download/nginx-1.15.12.tar.gz

RUN tar -xzvf nginx-1.15.12.tar.gz

WORKDIR nginx-1.15.12

RUN ./configure \
    --sbin-path=/usr/bin/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log \
    --with-pcre \
    --pid-path=/var/run/nginx.pid \
    --with-http_ssl_module

RUN make && make install
FROM python:3.10.9-slim
WORKDIR /BUGBITEDT_MAIN
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        libopencv-dev \ 
        build-essential \
        libssl-dev \
        libpq-dev \
        libcurl4-gnutls-dev \
        libexpat1-dev \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# Set environment variable
ENV TF_ENABLE_ONEDNN_OPTS=0
# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pipenv --upgrade

# Expose port
EXPOSE 8000

# Copy source code
COPY . .

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
