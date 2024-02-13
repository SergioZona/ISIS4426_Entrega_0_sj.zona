import datetime
from flask_restful import Resource
from ..models import db, User, UserSchema, Category, CategorySchema, Task, TaskSchema, State
from flask import request
from flask_jwt_extended import jwt_required, create_access_token

user_schema = UserSchema()
category_schema = CategorySchema()
task_schema = TaskSchema()

class UsersView(Resource):
    @jwt_required()
    def get(self):
        return [user_schema.dump(user) for user in User.query.all()]

    def post(self):
        #Create attributes that exists:
        json_data = request.get_json()

        username = json_data.get('username')
        password = json_data.get('password')        
        image = json_data.get('image')

        new_user = User(
            username=username,
            password=password,
            image=image          
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201

class UserView(Resource):
    @jwt_required()
    def get(self, user_id):
        tasks_by_user = Task.query.filter_by(user_id=user_id).all()
        return [task_schema.dump(task) for task in tasks_by_user]

class LoginView(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            access_token = create_access_token(identity=username)
            return { 'access_token': access_token }, 200
        else:
            return { 'message': 'Invalid username or password' }, 401
        
class CategoriesView(Resource):
    @jwt_required()
    def get(self):
        return [category_schema.dump(category) for category in Category.query.all()]

    @jwt_required()
    def post(self):
        new_category = Category(
            name=request.get_json()['name'],
            description=request.get_json()['description']
        )
        db.session.add(new_category)
        db.session.commit()
        return category_schema.dump(new_category), 201

class CategoryView(Resource):
    @jwt_required()
    def delete(self, category_id):
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return { "message":"Category deleted" }, 204
    
class TasksView(Resource):
    @jwt_required()
    def get(self):
        return [task_schema.dump(task) for task in Task.query.all()]

    @jwt_required()
    def post(self):
        #Create attributes that exists:
        json_data = request.get_json()

        text = json_data.get('text')
        creation_date = json_data.get('creation_date')
        
        due_date = json_data.get('due_date')
        if due_date:
            due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')  # Parse due_date to DateTime

        category_id = json_data.get('category_id')
        user_id = json_data.get('user_id')
        state = json_data.get('state')
        
        new_task = Task(
            text=text,
            creation_date=creation_date,
            due_date=due_date,
            category_id=category_id,
            user_id=user_id,
            state=state
        )
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task), 201

class TaskView(Resource):
    @jwt_required()
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return task_schema.dump(task)

    @jwt_required()
    def put(self, task_id):
        #Create attributes that exists:
        json_data = request.get_json()

        text = json_data.get('text')
        creation_date = json_data.get('creation_date')
        if creation_date:
            creation_date = datetime.datetime.strptime(creation_date, '%Y-%m-%d')  # Parse creation_date to DateTime
        
        due_date = json_data.get('due_date')
        if due_date:
            due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')  # Parse due_date to DateTime

        category_id = json_data.get('category_id')
        user_id = json_data.get('user_id')
        state = json_data.get('state')
        

        task = Task.query.get_or_404(task_id)
        task.text = text
        task.creation_date = creation_date
        task.due_date = due_date
        task.category_id = category_id
        task.user_id = user_id
        task.state = state
        db.session.commit()
        return task_schema.dump(task), 200

    @jwt_required()
    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return { "message":"Task deleted" }, 204
    