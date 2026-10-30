FROM alpine:latest
RUN apk add --no-cache curl unzip bash
RUN curl -L -o /app.zip https://github.com/XTLS/Xray-core/releases/download/v1.8.24/Xray-linux-64.zip && unzip /app.zip -d /usr/local/bin/ && rm /app.zip
COPY config.json /etc/xray/config.json
CMD ["/usr/local/bin/xray", "-c", "/etc/xray/config.json"]
