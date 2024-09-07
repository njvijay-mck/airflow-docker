# Apache Airflow Project

This project sets up an Apache Airflow environment using Docker, with custom configurations and additional Python dependencies for data processing and machine learning tasks.

## Overview

This Apache Airflow setup is designed for orchestrating and managing data workflows. It uses Docker to create a scalable and reproducible environment, including:

- Apache Airflow 2.10.0
- PostgreSQL 13 as the metadata database
- Redis 7.2 for task queueing
- Custom Python dependencies for data analysis and machine learning

## Features

- Fully dockerized Apache Airflow setup
- CeleryExecutor configuration for distributed task execution
- Custom Dockerfile for extending the official Airflow image
- Additional Python packages: pandas, numpy, and scikit-learn
- Configurable environment variables for easy customization

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Start the Airflow services:
   ```bash
   docker-compose up -d
   ```

3. Access the Airflow web interface at `http://localhost:8080`
   - Default username: airflow
   - Default password: airflow

## Project Structure

- `Dockerfile`: Custom Airflow image definition
- `docker-compose.yaml`: Docker Compose configuration for all services
- `requirements.txt`: Additional Python dependencies
- `dags/`: Directory for your Airflow DAG files
- `logs/`: Airflow logs directory
- `plugins/`: Custom Airflow plugins directory
- `config/`: Custom Airflow configuration files (if needed)

## Configuration

### Environment Variables

Key environment variables that can be modified:

- `AIRFLOW_IMAGE_NAME`: Docker image for Airflow (default: apache/airflow:2.10.0)
- `AIRFLOW_UID`: User ID for Airflow containers (default: 50000)
- `_AIRFLOW_WWW_USER_USERNAME`: Admin username (default: airflow)
- `_AIRFLOW_WWW_USER_PASSWORD`: Admin password (default: airflow)

### Custom Python Dependencies

Additional Python packages are specified in `requirements.txt`:
- pandas (2.1.4)
- numpy (1.26.2)
- scikit-learn (1.5.1)

To add more packages, update the `requirements.txt` file and rebuild the Docker image.


