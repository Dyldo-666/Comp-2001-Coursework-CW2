# COMP2001 CW2 - ProfileService

GitHub Username: <YOUR_GITHUB_USERNAME>  
Docker Image: <DOCKER_USERNAME>/<IMAGE_NAME>:latest

## Overview
This repository contains the ProfileService microservice for the Trail Application scenario (COMP2001).
It stores user profile data in SQL Server (schema CW2) and exposes REST endpoints via FastAPI.

Passwords are not stored. Authentication is handled by the provided Authenticator API.

## Tech
- Python (FastAPI)
- MS SQL Server (hosted university server)
- Docker (containerised deployment)
- Swagger UI at `/docs`

## Environment Variables
Set these when running locally or in Docker:

- DB_SERVER=dist-6-505.uopnet.plymouth.ac.uk
- DB_DATABASE=<your_db_name>
- DB_USERNAME=<your_username>
- DB_PASSWORD=<your_password>

Optional:
- CORS_ORIGINS=*
- AUTH_TIMEOUT=10

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
