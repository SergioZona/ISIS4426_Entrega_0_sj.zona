import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(80), nullable=True)
    tasks = db.relationship('Task', backref='user', cascade='all, delete, delete-orphan', lazy=True)

    def __repr__(self):
        return '<User: %r>' % self.id ,self.username, self.password, self.image

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    tasks = db.relationship('Task', backref='category', lazy=True, cascade='save-update, merge, refresh-expire')

    def __repr__(self):
        return '<Category: %r>' % self.id, self.name, self.description
    
class State(enum.Enum):
    SIN_EMPEZAR = 'Sin Empezar'
    EMPEZADA = 'Empezada'
    FINALIZADA = 'Finalizada'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    # State with three options: "Sin Empezar", "Empezada", "Finalizada"
    state = db.Column(db.Enum(State), nullable=True)
    
    def __repr__(self):
        return '<Task: %r>' % self.id, self.name, self.creation_date, self.due_date, self.category_id, self.state
    
class EnumState(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return { 'key': value.name, 'value': value.value }

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True   
        load_instance = True
        
class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_relationships = True
        load_instance = True

class TaskSchema(SQLAlchemyAutoSchema):
    state = EnumState(attribute='state')
    class Meta:
        model = Task
        include_relationships = True
        load_instance = True