from schema import Schema, And, Optional   
from datetime import datetime

data_schema = Schema(
   {
        'date': datetime,
        'name': And(str, len),
        'bool': bool
   }
)


data = {
    'date': datetime.utcnow(),
    'name': 'g',
    'bool': False
}

print(data_schema.is_valid(data))