FROM python:3
ADD . /dummy
WORKDIR /dummy
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["./gunicorn.sh"]
