FROM python:3.8

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml
COPY ./hello_world /code/hello_world

RUN pip install .
RUN pip install uvicorn

USER 1001

CMD ["python", "-m", "uvicorn", "hello_world:app", "--host", "0.0.0.0", "--port", "8080"]