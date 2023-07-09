# Next.js + FastAPI web app template
## Consists of:
- Next.js frontend (+tailwind)
- FastAPI backend
- Everything in Docker Compose
- Logging into files with fluentd docker driver

When using dev.docker-compose.yaml everything hot-reloaded (frontend needs manual reload in browser)

Recommended command to run
```
docker-compose -f "dev.docker-compose.yaml" up --build --force-recreate -d
```

## Todo
- Output logs in a more readable form
