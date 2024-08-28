class BaseMongoModel:
    def __init__(self, obj: dict):
        for key, value in obj.items():
            if key == "_id":
                self.id = str(value)
            elif isinstance(value, float):
                self.__setattr__(key, float(value))
            elif isinstance(value, bool):
                self.__setattr__(key, bool(value))
            elif isinstance(value, str):
                self.__setattr__(key, str(value))


class userInfoModel(BaseMongoModel):
    id: str = None
    firstName: str = None
    lastName: str = None
    email: str = None
    password: str = None
