# Use the slim version of Python 3
FROM python:3.10.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget nano git openssh-client && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get upgrade -y

RUN pip install jupyter

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES all

ENV CUDA_LAUNCH_BLOCKING 1

RUN mkdir /workspace
RUN echo "umask 002" >> /etc/profile
RUN chmod -R 777 /workspace

RUN ssh-keygen -t rsa -b 4096 -f /root/.ssh/id_rsa -N ""
RUN eval $(ssh-agent -s) && ssh-add /root/.ssh/id_rsa

RUN chmod 700 /root/.ssh && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 644 /root/.ssh/id_rsa.pub

WORKDIR /workspace

CMD ["jupyter", "notebook", "--NotebookApp.token=''", "--NotebookApp.password=''", "--ip=0.0.0.0", "--allow-root"]

EXPOSE 8888