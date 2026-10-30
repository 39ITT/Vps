FROM ghcr.io/xtls/xray-core:latest AS xray
FROM python:3.9-slim
COPY --from=xray /usr/local/bin/xray /usr/local/bin/xray
COPY config.json /etc/xray/config.json
RUN echo '#!/bin/bash\n\
python3 -m http.server 8080 &\n\
xray -c /etc/xray/config.json &\n\
wait' > /start.sh && chmod +x /start.sh
EXPOSE 8000
CMD ["/start.sh"]
