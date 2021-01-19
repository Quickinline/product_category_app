FROM python:3.6-alpine3.12

WORKDIR /app

# Building from source and Installing psycopg2 here

# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev \
#     && pip install --upgrade pip \
#     && pip install psycopg2-binary==2.8.4


# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


# Now copy in our code, and run it
COPY . /app
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]