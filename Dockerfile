FROM python:3.7.5-slim
RUN python -m pip install \
        Flask \
        realpython-reader
