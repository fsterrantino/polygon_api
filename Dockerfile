# Airflow image
FROM apache/airflow:2.3.3

# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt