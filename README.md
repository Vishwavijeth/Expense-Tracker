# Expense-Tracker

## Overview
The Daily expense sharing application helps user track and share thier daily expense. Users will be able to create account and log the expenses. This application ensures data validation, provides a RESTful api for ease of use.

## Installation

### Steps

  1. Clone the repository:
     ```bash
     git clone https://github.com/Vishwavijeth/Expense-Tracker

  2. Install the dependencies:
     ```bash
     pip install -r requirements.txt

  3. Run the application
     ```bash
     uvicorn main:app --reload

## API Endpoints
- [Authentication](https://github.com/Vishwavijeth/Expense-Tracker/blob/main/route/route.md)

- [Enpenses](https://github.com/Vishwavijeth/Expense-Tracker/blob/main/route/expense.md)

## Models

  User
  ```bash
class User(base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password =  Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    name = Column(String)
    phone = Column(String)
    expenses = relationship('Expense', back_populates='owner')
```

  Expense
  ```bash
class Expense(base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    split_method = Column(String, nullable=False)
    split_details = Column(JSON, nullable=False)
    owner = relationship('User', back_populates='expenses')
```

## Error Handling

### Split Type Error Handling

#### Total percentage Error
Ensure the total percentage of all participants in an expense adds up to 100%

### Error Response
```bash
{
  "detail" : "The sum of percentages must equal 100%"
}
```

#### Total Amount error
Ensure the total amount specified is equal to the sum of the amounts for each participant

### Error Response
```bash
{
  "detail" : "Sum of distributed amounts should be equal to the actual amount"
}
```

## Validation

### Email Validation
Emails are validated using Pydantic's **EmailStr** type
```bash
email: EmailStr
```

### Phone Number Validation
Mobile numbers are validated to ensure they are exactly 10 digits long:
```bash
phone_number: Annotated[str, StringConstraints(max_length=10, min_length=10, pattern=r'^\d{10}$')]
```

