# COMP2001 CW2 - ProfileService

## Github Repository
https://github.com/Dyldo-666/Comp-2001-Coursework-CW2

## Docker Image
Docker Hub image:
dylbo666/profileservice-cw2:latest

To run:
docker pull dylbo666/profileservice-cw2:latest
docker run -p 8000:8000 \
  -e DB_SERVER=dist-6-505.uopnet.plymouth.ac.uk,1433 \
  -e DB_DATABASE=COMP2001_DMoore \
  -e DB_USERNAME=*** \
  -e DB_PASSWORD=*** \
  dylbo666/profileservice-cw2:latest

## Overview
This repository contains the ProfileService microservice for the Trail Application scenario (COMP2001).
It stores user profile data in SQL Server (schema CW2) and exposes REST endpoints via FastAPI.

Passwords are not stored. Authentication is handled by the provided Authenticator API.

## Tech
- Python (FastAPI)
- MS SQL Server (hosted university server)
- Docker (containerised deployment)
- Swagger UI at `/docs`

