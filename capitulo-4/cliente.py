class Cliente:
    def __init__(self, id: int, name: str, age: int, email: str):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__email = email

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name= value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value: str):
        self.__age = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value: str):
        self.__email = value
    

    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "age": self.__age,
            "email": self.__email
        }







