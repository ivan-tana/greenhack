from schema import Schema, And, Optional   

user_data_schema = Schema({
    'fname': And(str, len),
    'lname': And(str, len),
    Optional('address'): And(str, len),
    'active': And(str, len),
    'email': And(str, len),
    'user_type': And(str, len),
    'profile_image': And(str, len),
    'tel': And(str, len),
    'birthday': And(str, len),

})