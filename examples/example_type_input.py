from py_helpers.base.type_input import type_input

INPUT_TYPE = int

val, message = type_input(
    input_type = INPUT_TYPE,
    input_message = "Please enter an integer : ",
)

try:
    assert (type(val) == INPUT_TYPE), "Wrong value entered"
    print(message)
    print(f"Value : {val}")
    print(f"Type of {val} : {type(val)}")
except AssertionError as e:
    print(f"Error : {str(e)}")
