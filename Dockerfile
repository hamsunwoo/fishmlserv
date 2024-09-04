FROM hamsunwoo/fishmlserv:1.1.0

WORKDIR /code

#COPY . /code/
COPY src/fishmlserv/main.py /code/
#COPY requirements.txt /code/

#RUN 모델 서빙만(의존성의 위 BASE 이미지에서 모두 설치했다.)
RUN pip install --no-cache-dir --upgrade git+https://github.com/hamsunwoo/fishmlserv.git@1.1.1/k

#모델 서빙을 위해 API 구동을 위한 FastAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
