from schema import Schema, And, Optional


user_data_schema = Schema(
    {
        'fname': And(str, len),
        Optional('lname'): And(str, len),
    }
)

data = {
    "fname": "john"
}

print(user_data_schema.validate(data))