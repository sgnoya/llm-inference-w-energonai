FROM hpcaitech/colossalai:0.1.10-torch1.11-cu11.3

RUN git clone https://github.com/hpcaitech/EnergonAI.git && \
    cd EnergonAI && \
    pip install -r requirements.txt && \
    pip install . && \
    cd examples/opt && \
    pip install -r requirements.txt

RUN pip3 install bitsandbytes==0.35.0