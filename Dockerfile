FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip==21.3.1
RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app/

RUN cd /home/ubuntu/app
ADD . .

RUN pip install -r requirements.txt
RUN pytest -vv || exit 1
# for production please remove --reload
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]
