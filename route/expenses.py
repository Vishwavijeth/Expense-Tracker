from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.responses import FileResponse
from db.database import sessionLocal
from typing import Annotated, Dict
from sqlalchemy.orm import Session
from db.models import User, Expense
from pydantic import BaseModel
from utils import Split_Equal, Split_Exact, Split_Percentage
from route.auth import Get_current_user
from io import StringIO
import csv

route = APIRouter(prefix='/expense', tags=['expense'])

def Get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(Get_db)]
user_dependency = Annotated[dict, Depends(Get_current_user)]


class CreateExpense(BaseModel):
    description: str
    amount: float
    split_method: str
    split_details: Dict[str, float]
    
@route.get('/get_all_expenses', status_code=status.HTTP_200_OK)
def GetAllExpense(db: db_dependency):
# Returns all the expenses of all the user
    return db.query(Expense).all()
    
@route.post('/create_expense', status_code=status.HTTP_200_OK)
def CreateExpense(db: db_dependency, expense: CreateExpense, user: user_dependency):
    #  this method is used to create a new expense for a particular user
    #  this method also includes user authentication
    
    if user is None: # checks for user, authenticated or not
        raise HTTPException(404, detail="Expense cannot be added, User not found")
    
    #  now if user is authenticated we insert the expense into the Expense table for the respestive user
    newExpense = Expense(**expense.model_dump(), owner_id = user.get('id'))
    
    db.add(newExpense)
    db.commit()
    
    #  conditions for the Split methods 
    if expense.split_method == 'Equal':
        newExpense.split_details = Split_Equal(expense.split_details, expense.amount)
    elif expense.split_method == 'Exact':
        newExpense.split_details = Split_Exact(expense.split_details, expense.amount)
    elif expense.split_method == 'Percentage':
        newExpense.split_details = Split_Percentage(expense.split_details, expense.amount)
        
    db.add(newExpense)
    db.commit()
    
    return newExpense

@route.get('/user_expense/{userid}', status_code=status.HTTP_200_OK)
def GetUserExpense(db: db_dependency, userid: int):
    
    #  this method is used to get the expense details for a particular used based on the used id provided
    
    expense_model = db.query(Expense).filter(Expense.owner_id == userid).all()
    
    if expense_model is None:
        return HTTPException(404, detail='No expense found for this user')
    
    return expense_model

@route.get("/balance_sheet/download", response_class=FileResponse)
def download_balance_sheet(db: Session = Depends(Get_db)):
    
    #  this method is used to download the balance sheet that includes the expense details of all the users
    
    expenses = db.query(Expense).all()
    balance_sheet = []

    for expense in expenses:
        user = db.query(User).filter(User.id == expense.owner_id).first()
        balance_sheet.append({
            'user': user.name,
            'email': user.email,
            'description': expense.description,
            'amount': expense.amount,
            'split_method': expense.split_method,
            'split_details': expense.split_details
        })

    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['User', 'Email', 'Description', 'Amount', 'Split Method', 'Split Details'])
    cw.writerows([(row['user'], row['email'], row['description'], row['amount'], row['split_method'], row['split_details']) for row in balance_sheet])

    output = Response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=balance_sheet.csv"
    output.headers["Content-type"] = "text/csv"
    return output
