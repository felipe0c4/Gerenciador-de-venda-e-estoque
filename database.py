from peewee import *


db = SqliteDatabase('database.db')

db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Login(BaseModel):
    usuario = CharField()
    senha = CharField()
    admin = BooleanField()

class Produtos(BaseModel):
    item = CharField()
    preco = FloatField()
    quantidade = IntegerField()

class Vendas(BaseModel):
    item = CharField()
    preco = FloatField()
    quantidade = IntegerField()



db.create_tables([Login, Produtos, Vendas])
