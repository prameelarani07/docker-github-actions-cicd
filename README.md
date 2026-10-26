# CI/CD Pipeline with GitHub Actions & Docker

## Introduction

This project demonstrates an automated CI/CD pipeline for a Flask web application using GitHub Actions, Docker, and Docker Hub. It automates application testing, Docker image building, and image publishing.

## Project Features

- Flask-based DevOps dashboard.
- Automated tests using pytest.
- Docker containerization.
- GitHub Actions workflow for continuous integration and delivery.
- Automatic Docker image publishing to Docker Hub after successful tests.
- Local application deployment using Docker.
- Health-check endpoint to verify application status.
- Multi-platform Docker image support for AMD64 and ARM64.

## Tools Used

- Python and Flask
- pytest
- Docker
- Git and GitHub
- GitHub Actions
- Docker Hub

## CI/CD Workflow

1. Push code to the GitHub repository.
2. GitHub Actions checks out the source code.
3. Python dependencies are installed.
4. Automated tests run using pytest.
5. If the tests pass and code is pushed to `main`, Docker builds the image.
6. The Docker image is published to Docker Hub.
7. The image is pulled and run locally using Docker.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/prameelarani07/docker-github-actions-cicd.git
cd docker-github-actions-cicd
```

### 2. Create and activate a virtual environment (optional)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies and run tests

```bash
pip install -r requirements.txt
python -m pytest -v
```

### 4. Run the application

```bash
python app.py
```

Open http://localhost:5000 in your browser.

## Run with Docker

Pull the published image:

```bash
docker pull prameelarani0712/docker-github-actions-cicd:latest
```

Start the container:

```bash
docker run -d --name devops-cicd-container -p 5001:5000 prameelarani0712/docker-github-actions-cicd:latest
```

Open the dashboard at http://localhost:5001.

Check the health endpoint at http://localhost:5001/health.

To stop and remove the container:

```bash
docker rm -f devops-cicd-container
```

## Project Links

- **GitHub Repository:** https://github.com/prameelarani07/docker-github-actions-cicd
- **Docker Hub Image:** https://hub.docker.com/r/prameelarani0712/docker-github-actions-cicd

## Conclusion

This project provides practical experience with automated testing, Docker containerization, GitHub Actions workflows, Docker Hub image publishing, and local deployment.
