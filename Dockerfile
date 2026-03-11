FROM python:3.12-slim

WORKDIR /app

# Copy only the pyproject.toml files for dependency installation
COPY app/pyproject.toml ./app/
COPY pyproject.toml ./

# Install dependencies from app/pyproject.toml
RUN pip install --no-cache-dir -e ./app

# Copy the rest of the project
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app/main.py"]
