FROM ubuntu:latest

LABEL cp-requests latest

VOLUME [ "/mnt" ]

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git && \
    pip3 install requests && \
    git clone https://github.com/ryanrasmuss/cp-requests && \
    apt-get autoremove --purge -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR cp-requests/

CMD ["/bin/bash"]
