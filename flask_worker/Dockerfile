# syntax=docker/dockerfile:1

FROM python:3.9.10-slim-buster

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 3000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=3000" ]

