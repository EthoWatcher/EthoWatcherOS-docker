FROM mongo
RUN apt-get update &&\
    apt-get install -y wget
# RUN mkdir /usr/app
# COPY miniconda.sh /usr/app
# RUN bash /usr/app/miniconda.sh -b -p /opt/conda

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH
RUN cd $CONDA_DIR/bin && conda init 
RUN pip install pymc3
RUN pip install notebook

RUN  mkdir /home/ethowatcher/
RUN  cd /home/ethowatcher/
WORKDIR /home/ethowatcher/

COPY --chown=developer:developer ./analise_dados/ /home/ethowatcher/analise_dados
COPY --chown=developer:developer ./gestao_dados/ /home/ethowatcher/gestao_dados
RUN pip install -e /home/ethowatcher/gestao_dados/gestao-dados/




# exposing jupyter
EXPOSE 8888
# exposing db port
EXPOSE 27017


CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--port", "8888", "--allow-root" ]