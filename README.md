
1. Download model
   1. git lfs install
   2. git clone https://huggingface.co/bigscience/bloom-3b
2. Build docker image
   1. docker build . -t colossalai
3. Run container
   1. docker run --gpus all  --rm -it -p 8020:8020 -v ./:/model_checkpoint -v ./:/config --ipc=host colossalai:latest
4. Run LLM server
   1. attach the container (docker attach container-name)
   2. cd /workspace/EnergonAI/examples/bloom
   3. python server.py --tp 1 --name /model_checkpoint/bloom-3b  --dtype "int8" --http_port 8020
5. Run chat client in an another terminal
   1. pip install streamlit
   2. streamlit run bloom_client.py
