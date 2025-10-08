# Use a stable, lightweight Python image
FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files & Ensure Python output is not buffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies for LightGBM and optional libraries (like pyarrow, numpy, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . .

# Upgrade pip to avoid old dependency resolution issues
RUN pip install --upgrade pip

# Install dependencies in editable mode
RUN pip install --no-cache-dir -e .

# Train the model (if required at build time)
RUN python pipeline/training_pipeline.py

# Expose the port for Flask
EXPOSE 5000

# Command to run the app
CMD ["python", "application.py"]
