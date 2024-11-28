# Langchain Report Generator

This project is a Langchain Report Generator that uses FastAPI and Docker for containerization.

## Prerequisites

- Docker installed on your machine
- Docker Compose installed on your machine

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/langchain_report_generator.git
cd langchain_report_generator
```

### 2. Set Up Environment Variables
Create a .env file in the root directory of the project and add your Google API key (get from Google AI studio):
```
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Build the Docker Container
Use Docker Compose to build the container:
```
docker compose build
```

### 4. Run the Docker Container
Use Docker Compose to run the container:
```
docker compose up
```

### 5. Access the API
You can access the API endpoints using a tool like curl or Postman.

