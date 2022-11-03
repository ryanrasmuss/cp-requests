# cp-requests
# -----------
#
# Disk Requirements: ~ 500 mb
#
# To build: docker build -t cp-requests .
#
# To run: docker run -v $(``pwd``)/:/cp-requests/session/ cp-requests:latest [cmd] [parameters]
# ^^^ If you want to copy session.txt (stateful)

FROM ubuntu:kinetic-20220830

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

WORKDIR /cp-requests/
RUN mkdir session/

#CMD ["/bin/bash"]
ENTRYPOINT [ "./mgmt_api.sh" ]
