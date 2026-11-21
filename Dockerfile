FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/blink
COPY blink.py /opt/blink/blink.py

CMD ["python3", "/opt/blink/blink.py"]
