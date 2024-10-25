from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    ...  # точки заместо pass 🌚


class UserCreate(schemas.BaseUserCreate):
    ...


class UserUpdate(schemas.BaseUserUpdate):
    ...
