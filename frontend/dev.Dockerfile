FROM node:18-slim AS installer
WORKDIR /app
COPY package.json ./
RUN --mount=type=cache,target=/app/.npm \
    npm set cache /app/.npm && \
    npm install

FROM node:18-slim AS runner
WORKDIR /app
COPY . .
COPY --from=installer /app/node_modules ./node_modules
CMD npm start
