from pydantic import BaseModel, constr


class UserSchema(BaseModel):
    name: constr(max_length=30)
    password: constr(max_length=128)
    email: constr(max_length=254)

    class Config:
        orm_mode = True
