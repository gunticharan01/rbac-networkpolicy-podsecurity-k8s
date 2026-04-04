FROM python:3.11-slim AS base

# Create non-root user (required for PSA restricted mode)
RUN addgroup --system appgroup && adduser --system --group appuser

WORKDIR /app

# Install dependencies as root, then switch user
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY main.py .

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
