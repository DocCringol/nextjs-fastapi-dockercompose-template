FROM python:3.9-slim-buster AS installer
WORKDIR /app
COPY requirements.txt requirements.txt
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip \
	pip install -r requirements.txt

FROM python:3.9-slim-buster AS runner
WORKDIR /app
COPY --from=installer /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . .
CMD python main.py