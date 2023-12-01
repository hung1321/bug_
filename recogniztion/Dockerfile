
FROM ubuntu:18.04 as builder

# Install necessary dependencies for NGINX build
RUN apt-get update && apt-get install -y \
    build-essential \
    libpcre3 \
    libpcre3-dev \
    zlib1g \
    zlib1g-dev \
    libssl-dev \
    wget

# Download and build NGINX
WORKDIR /nginx
RUN wget http://nginx.org/download/nginx-1.15.12.tar.gz && \
    tar -xzvf nginx-1.15.12.tar.gz && \
    cd nginx-1.15.12 && \
    ./configure \
        --sbin-path=/usr/bin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --with-pcre \
        --pid-path=/var/run/nginx.pid \
        --with-http_ssl_module && \
    make && make install

# Create the final image
FROM python:3.10.9-slim

# Set the working directory
WORKDIR /BUGBITEDT_MAIN

# Install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    libopencv-dev \
    build-essential \
    libssl-dev \
    libpq-dev \
    libcurl4-gnutls-dev \
    libexpat1-dev \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variable
ENV TF_ENABLE_ONEDNN_OPTS=0

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install pipenv --upgrade

# Expose port
EXPOSE 8000

# Copy source code
COPY . .

# Copy NGINX binary from the builder stage
COPY --from=builder /usr/bin/nginx /usr/bin/nginx

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

