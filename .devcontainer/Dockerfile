# Use the base image from devcontainers
FROM mcr.microsoft.com/devcontainers/python:1-3.13-bullseye

# Install LDAP development libraries and related dependencies
RUN apt-get update && apt-get install -y \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    python3-distutils \
    python3-dev \
    python3-pip \
    vim \
    netcat-traditional

# Install NodeJS and NPM
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs

# Unfuck timezones for Kerberos
#RUN ln -sf /usr/share/zoneinfo/Europe/Oslo /etc/localtime