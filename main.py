from fastapi import FastAPI
from db.database import engine
import db.models as models
import route.expenses as expenses, route.auth as auth

app = FastAPI()

models.base.metadata.create_all(bind = engine)

app.include_router(expenses.route)
app.include_router(auth.route)
