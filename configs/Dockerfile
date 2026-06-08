FROM python:3.12-slim

# install node (necessario per Pi)
RUN apt-get update && apt-get install -y \
    curl \
    git \
    bash \
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs

WORKDIR /workspace

# install pi coding agent globally
RUN npm install -g --ignore-scripts @earendil-works/pi-coding-agent

CMD ["bash"]