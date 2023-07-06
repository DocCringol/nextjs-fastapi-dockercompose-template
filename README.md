# Yet Another Template??? (give me a name, please)
## Consists of:
- Next.js fronted
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
- Add support of FastAPI Routes, instead of 2 APIs
- Output logs in a more readable form