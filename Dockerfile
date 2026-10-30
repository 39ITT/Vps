FROM ghcr.io/xtls/xray-core:latest
COPY config.json /etc/xray/config.json
CMD ["/usr/local/bin/xray", "-c", "/etc/xray/config.json"]
