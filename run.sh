docker build -t docker_frontend -f frontend/Dockerfile .
docker run -p 8501:8501 docker_frontend

docker build -t docker_backend -f backend/Dockerfile .
docker run -p 8000:8000 docker_backend

docker-compose up -d --build
docker-compose down
