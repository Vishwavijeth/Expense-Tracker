## Endpoints

### 1. /create_expense
This endpoint is for creating an expense for a user

### Request
**Method:** POST

**path:** /create_expense

### Response example
```bash
[
  {
    "owner_id": 1,
    "description": "string",
    "split_method": "Equal",
    "amount": 100,
    "id": 1,
    "split_details": {
      "additionalProp1": 33.333333333333336,
      "additionalProp2": 33.333333333333336,
      "additionalProp3": 33.333333333333336
    }
  }
]
```

### 2. /get_all_expenses
This endpoint is to get all the expenses by all the users

### Request
**Method:** GET

**path:** /get_all_expenses

### Response example
```bash
[
  {
    "owner_id": 1,
    "description": "string",
    "split_method": "Equal",
    "amount": 100,
    "id": 1,
    "split_details": {
      "additionalProp1": 33.333333333333336,
      "additionalProp2": 33.333333333333336,
      "additionalProp3": 33.333333333333336
    }
  },
  {
    "owner_id": 1,
    "description": "Dinner",
    "split_method": "Percentage",
    "amount": 200,
    "id": 2,
    "split_details": {
      "additionalProp1": 100,
      "additionalProp2": 50,
      "additionalProp3": 50
    }
  },
  {
    "owner_id": 1,
    "description": "Dinner",
    "split_method": "Percentage",
    "amount": 100,
    "id": 3,
    "split_details": {
      "additionalProp1": "50.0 %",
      "additionalProp2": "25.0 %",
      "additionalProp3": "25.0 %"
    }
  }
]
```

### 3. /banlance_sheet/download
This endpoint is to download the balance sheet

### Request
**Method:** GET

**path:** /balance_sheet/download

