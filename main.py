"""from pyscript import display, document


def getting_data(e):    # creating a function
    document.getElementById('output').innerHTML = ""
    username = document.getElementById('username').value # getting the data from an input field
    password = document.getElementById('password').value

    display(f'Your username is {username} and your password is {password}. Do you confirm?', target='output')
"""
"""# using arithmetic operators
from pyscript import display, document


def adding_numbers(e):
    addend1 = float(document.getElementById('num1').value)
    addend2 = float(document.getElementById('num2').value)
    sum = addend1 + addend2

    display(f'The sum of {addend1} and {addend2} is {sum}')
"""
#   solving trapezoid
from pyscript import display, document


def trapezoid_solving(e):
    document.getElementById('output').innerHTML = ""
    a = float(document.getElementById('base1').value)
    b = float(document.getElementById('base2').value)
    h = float(document.getElementById('height').value)
    area = (a+b)/2*h

    display(f'Area of Trapezoid: {area}.', target='output')