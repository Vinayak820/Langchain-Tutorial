from typing import TypedDict

class Person(TypedDict):
    age: int
    name: str

person: Person = {'age': 20, 'name': 'Vinayak'}

print(person)
