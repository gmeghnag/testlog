FROM docker.io/python:3.6-alpine
USER root
COPY . /testlog
RUN chgrp -R 0 /testlog \
    && chmod -R g=u /testlog
USER 1001
WORKDIR /testlog

ENTRYPOINT ["python"]
CMD ["app/app.py"]
