# Yet Another Template??? (give me a name, please)
## Consists of:
- ReactJS fronted
- FastAPI backend 
- Database API (on FastAPI again, for my own curtain purposes, easy to remove)
- Everything in Docker Compose
- Logging into files with fluentd docker driver

When using dev.docker-compose.yaml everything hot-reloaded (frontend needs manual reload in browser)

Recommended command to run
```
docker-compose -f "dev.docker-compose.yaml" up --build --force-recreate -d
```

## Todo
- FIX problem with reaching backend from frontend (probably some problem with docker networking)
- Output logs in a more readable form