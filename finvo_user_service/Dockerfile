FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# RUN curl -Ls https://astral.sh/uv/install.sh | bash && cp /root/.cargo/bin/uv /usr/local/bin/

RUN curl -L https://astral.sh/uv/install.sh | bash -x && cp /root/.cargo/bin/uv /usr/local/bin/

COPY . .

EXPOSE 8000

CMD ["uv", "run", "--", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
