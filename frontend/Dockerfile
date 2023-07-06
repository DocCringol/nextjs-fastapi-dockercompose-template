FROM node:18.16.1-slim AS installer
WORKDIR /app
COPY package.json ./
RUN --mount=type=cache,target=/app/.npm \
    npm set cache /app/.npm && \
    npm install

FROM node:18.16.1-slim AS builder
WORKDIR /app
COPY . .
COPY --from=installer /app/node_modules ./node_modules
RUN npm run build

FROM node:18.16.1-slim AS runner
WORKDIR /app
COPY --from=builder /app/build ./build
CMD npx serve -s build
