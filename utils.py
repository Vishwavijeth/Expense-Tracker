from typing import Dict

def Split_Equal(details: Dict, amount: float):
    
    new_amount = amount / len(details)
    
    for i in details.keys():
        details[i] = new_amount
    return details

def Split_Exact(details: Dict, amount: float):
    summ = sum(details.values())
    
    if summ != amount:
        raise ValueError('Sum of distributed amounts should be equal to the actual amount')
    
    return details

def Split_Percentage(details: Dict, amount: float):
    total_percentage = sum(details.values())
    
    if total_percentage != 100:
        raise ValueError('The sum of percentages must equal 100%')
    
    for i in details.keys():
        details[i] = f"{(details[i] / 100) * amount} %"
        
    return details

    