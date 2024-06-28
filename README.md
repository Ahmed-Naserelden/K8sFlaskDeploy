# K8sFlaskDeploy

## Overview

**K8sFlaskDeploy** is a simple project that demonstrates how to deploy a Flask application on a Kubernetes cluster using Minikube. The project involves containerizing the Flask application with Docker and managing its deployment and scaling using Kubernetes.

## Project Structure

- `app.py`: The main Flask application file.
- `Dockerfile`: The Dockerfile to build the Docker image for the Flask application.
- `deployment.yaml`: Kubernetes Deployment configuration file.
- `service.yaml`: Kubernetes Service configuration file.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ahmed-Naserelden/K8sFlaskDeploy.git

cd K8sFlaskDeploy
```

## 2. Build the Docker Image
Build the Docker image using the provided Dockerfile.

```bash
docker build -t yourdockerhubusername/flaskimg:v1 .
```

### 3. Push the Docker Image to Docker Hub
Log in to Docker Hub and push the image.

```bash
docker login
docker push yourdockerhubusername/flaskimg:v1
```

### 4. Start Minikube
Start Minikube to create a local Kubernetes cluster.

```bash
minikube start
```

### 5. Apply the Deployment Configuration
Apply the Kubernetes Deployment configuration to create the Flask application deployment.

```bash
kubectl apply -f deployment.yaml
```

### 6. Apply the Service Configuration
Apply the Kubernetes Service configuration to expose the Flask application.

```bash
kubectl apply -f service.yaml
```

### 7. Access the Flask Application
Use Minikube to access the Flask application service.

```bash
minikube service backend
```

## Conclusion

By following these instructions, you will have a Flask application running on a local Kubernetes cluster managed by Minikube. You can access the application through the browser and see the home and about pages, each served by different pods within the cluster. This setup demonstrates the basic principles of containerized application deployment, service exposure, and scaling using Kubernetes.

Feel free to explore and modify the project to suit your needs. Happy coding!