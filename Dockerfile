from jupyter/datascience-notebook:python-3.10.6 

workdir /workdir
expose 8888

# python package installation.
run pip install japanize-matplotlib && \
    pip install ipynb_path && \
    pip install jupyterlab_vim && \
    pip install openpyxl

run pip install contextplt && \
    pip install cmocean && \
    pip install watermark && \
    pip install networkx


