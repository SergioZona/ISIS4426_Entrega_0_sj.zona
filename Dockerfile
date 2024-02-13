FROM python

RUN pip install flask
RUN pip install flask-restful
RUN pip install flask-marshmallow
RUN pip install flask_sqlalchemy
RUN pip install marshmallow_sqlalchemy
RUN pip install flask_jwt_extended
RUN pip install asgiref
RUN pip install hypercorn

COPY . .

EXPOSE 5000

CMD hypercorn flaskr.app:asgi_app --bind localhost:5000