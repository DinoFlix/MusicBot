# Python 3.10 image use kar rahe hain
FROM python:3.10

# Work directory set karo
WORKDIR /app

# Dependencies copy karo
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Application code copy karo
COPY . .

# Application ko run karne ke liye command
CMD ["python", "main.py"]  # Replace 'main.py' with your entry file
