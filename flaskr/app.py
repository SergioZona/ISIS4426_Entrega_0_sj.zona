from asgiref.wsgi import WsgiToAsgi
from flaskr import create_app
from flask_restful import Api
from .models import db, User, Category, Task 
from .models import UserSchema, CategorySchema, TaskSchema, State
from datetime import datetime
from .views import UsersView, UserView, LoginView, CategoriesView, CategoryView, TasksView, TaskView
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(UsersView, '/usuarios')
api.add_resource(LoginView, '/usuarios/iniciar-sesion')

api.add_resource(CategoriesView, '/categorias')
api.add_resource(CategoryView, '/categorias/<int:category_id>')

api.add_resource(TasksView, '/tareas/')
api.add_resource(UserView, '/tareas/usuario/<int:user_id>')
api.add_resource(TaskView, '/tareas/<int:task_id>')

jwt = JWTManager(app)

asgi_app = WsgiToAsgi(app)