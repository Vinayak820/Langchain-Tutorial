from typing import TypedDict
# It does not validate, It just tell that, Ok! This is the expected datatype.
# class Person(TypedDict):

#     name: str
#     age: int

# new_person: Person = {'name':'Vinayak', 'age':21}
# print(new_person)


class Person(TypedDict):
    name: str
    age: int
    
input = {'name':'Vinayak', 'age':21}

# new_person = Person(input)
new_person = Person(**input)
print(new_person)
