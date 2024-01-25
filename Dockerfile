# Airflow image
FROM apache/airflow:2.3.3

# Copy requirements.txt into the container
COPY requirements.txt .
COPY ./dist/scripts-1.0.0-py3-none-any.whl .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt
