# Custom Health App

A simple FastAPI application for testing health check endpoints. This image is on [Docker Hub](https://hub.docker.com/r/syaffers/custom-health-app).

## Quick Start

### Default health check endpoint

```bash
docker run -d -p 8080:8080 syaffers/custom-health-app:latest
```

The API will be available at `http://localhost:8080` and the default health check route is `/is_healthy`.

### Custom health check endpoint

_NOTE: Only in version 0.3.0 and above_

```bash
docker run -d -p 8080:8080 -e HEALTH_CHECK_ENDPOINT=/healthz syaffers/custom-health-app:latest
```

Now the health check route is served at `/healthz`.

## Features

- Health check endpoint at `/is_healthy`: Returns service status (configurable via `HEALTH_CHECK_ENDPOINT` env var)
- Prediction endpoint at `/predict`: Uppercases text input
- Metrics endpoint at `/metrics`: Returns CPU and memory usage

## Image details

- Base Image: `tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim`
- Exposed Port: `8080`

## Usage

### Health Check

```bash
curl http://localhost:8080/is_healthy
```

Response:
```json
{
  "status": "ok"
}
```

### Text Processing

```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "héllo world"}'
```

Response:
```json
{
  "output": "HÉLLO WORLD"
}
```

### System Metrics

```bash
curl http://localhost:8080/metrics
```

Response:
```json
{
  "cpu_usage": 2.5,
  "memory_usage": 45.3
}
```

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`
