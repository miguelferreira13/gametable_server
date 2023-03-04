# Use the official lightweight Python image.
FROM python:3.9-slim
# Allow statements and log 
ENV PYTHONUNBUFFERED True
# Copy local code to the container image.
ENV APP_HOME=/app \
    PORT=8080 \
    WS=wss://gametable-xolpakqy5q-ez.a.run.app/notsober/wss \
    WS_TYPE=wss \
    URL=https://gametable-xolpakqy5q-ez.a.run.app

WORKDIR $APP_HOME
COPY . ./
# Install production dependencies.
RUN pip install -r requirements.txt

# Run
CMD ["python", "setup.py"]