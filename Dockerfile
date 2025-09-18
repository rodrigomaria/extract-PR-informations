FROM python:3.13-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and HTML files
COPY . .

# Set the entrypoint to run the script
ENTRYPOINT ["python", "extract_titles.py"]
