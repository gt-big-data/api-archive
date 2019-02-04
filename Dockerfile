FROM python:3.7-alpine

# Copy the source code into the current dir
COPY requirements.txt .

# Install from the prod-requirements.txt and delete it from the image
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

# Copy the srouce code over
COPY src .

# Expose a port for the webserver
EXPOSE 9001

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:9001", "app:app"]