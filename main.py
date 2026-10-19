# Dealing with Sets
from pyscript import document, display


def get_name(e):
    document.getElementById('div1').innerHTML = ''
    first_name = document.getElementById('fname').value
    last_name = document.getElementById('lname').value
    full_name = first_name + last_name


    grade_7 = {'Lorraine Smith', "Hailey Chang"}
    grade_8 = {'Zayn Aliah', 'Jesse Pinkman'}
    grade_9 = {'Sully Thurman', 'Joaquin Villar'}
    grade_10 = {'Macy Panela', 'Joaquin Tabije'}


    members = (grade_7 | grade_8 | grade_9 | grade_10)
    members.add(full_name)



    display(f'List of members {members} amount of members {len(members)}', target='div1')