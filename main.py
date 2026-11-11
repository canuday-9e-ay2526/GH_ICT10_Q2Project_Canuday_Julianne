#Math Club checker
from pyscript import display, document

def view_member(e):
    #Get input values
    document.getElementById('result').innerHTML = ' '
    student_first = document.getElementById('firstname').value
    student_last = document.getElementById('lastname').value

    student_name = str(student_first) + " " + str(student_last) # Combine input values

    Math_members = ['Aisha Padua', 'Julianne Canuday', 'Pocholo Commanda', 'Jesse Villante', 'Dwayne Chua', 'Rachmiel Lozada', 'Alonzo Paulino', 'Zoe Laquindanum', 'Clarisse Casal', 'Zedric Ramirez', 'Megan Ty', 'Reina Fortaleza']
    member_checker = student_name in Math_members # checks boolean 0 or 1

    #Display output
    display_message = (f'Sorry, you are not included in Math club', f'Congratulations {student_name}, you are part of Math club')
    display(display_message[member_checker], target='result')

def add_member(e):
    #Get input values
    document.getElementById('result').innerHTML = ' '
    student_first = document.getElementById('firstname').value
    student_last = document.getElementById('lastname').value

    student_name = str(student_first) + " " + str(student_last) # Combine input values

    # All sets
    Teacher = {'Louise Ferma'}
    G10 = {'Aisha Padua', 'Julianne Canuday', 'Pocholo Commanda', 'Jesse Villante', 'Dwayne Chua', 'Rachmiel Lozada', 'Alonzo Paulino'}
    G11 = {'Clarisse Casal'}
    G12= {'Zoe Laquindanum',  'Zedric Ramirez', 'Megan Ty', 'Reina Fortaleza'}

    Math_Complete = G10 | G11 | G12 | Teacher # Union - Join sets
    Math_Complete.add(student_name) # Add input
   
    

    #Display output
    display(f'Here is a list of All the members: {Math_Complete}', target='result') # Displays all members

    display(f'There are {len(Math_Complete)} Members Total', target='result') # Displays Number of members

    #Math Club checker
from pyscript import display, document

def check_element(e):
    #Get input values
    document.getElementById('result').innerHTML = ' '
    element = document.getElementById('Element').value.strip().capitalize()
    #Elements:
    Element_list = {
        'H': {
            'Symbol': 'H',
            'Element': 'Hydrogen',
            'Atomic Number': '1',
            'Atomic Mass': '1.00784'
        },
        'He': {
            'Symbol': 'He',
            'Element': 'Helium',
            'Atomic Number': '2',
            'Atomic Mass': '4.0026'
        },
         'C': {
            'Symbol': 'C',
            'Element': 'Carbon',
            'Atomic Number': '6',
            'Atomic Mass': '12'
        },
         'N': {
            'Symbol': 'N',
            'Element': 'Nitrogen',
            'Atomic Number': '7',
            'Atomic Mass': '14'
        },
         'O': {
            'Symbol': 'O',
            'Element': 'Oxygen',
            'Atomic Number': '8',
            'Atomic Mass': '16'
        },
         'F': {
            'Symbol': 'F',
            'Element': 'Fluorine',
            'Atomic Number': '9',
            'Atomic Mass': '18.998'
        },
         'P': {
            'Symbol': 'P',
            'Element': 'Phosphorus',
            'Atomic Number': '15',
            'Atomic Mass': '30'
        },
         'S': {
            'Symbol': 'S',
            'Element': 'Sulfur',
            'Atomic Number': '16',
            'Atomic Mass': '32'
        },
         'Cl': {
            'Symbol': 'Cl',
            'Element': 'Chlorine',
            'Atomic Number': '17',
            'Atomic Mass': '35'
        },
         'Se': {
            'Symbol': 'Se',
            'Element': 'Selenium',
            'Atomic Number': '34',
            'Atomic Mass': '78.960'
        },
         'Br': {
            'Symbol': 'Br',
            'Element': 'Bromine',
            'Atomic Number': '35',
            'Atomic Mass': '79.904'
        },
         'I': {
            'Symbol': 'I',
            'Element': 'Iodine',
            'Atomic Number': '53',
            'Atomic Mass': '126.90'
        },
         'Ne': {
            'Symbol': 'Ne',
            'Element': 'Neon',
            'Atomic Number': '10',
            'Atomic Mass': '20.180'
        },
         'Ar': {
            'Symbol': 'Ar',
            'Element': 'Argon',
            'Atomic Number': '18',
            'Atomic Mass': '39.148'
        },
         'Kr': {
            'Symbol': 'Kr',
            'Element': 'Krypton',
            'Atomic Number': '36',
            'Atomic Mass': '83.798'
        },
         'Xe': {
            'Symbol': 'Xe',
            'Element': 'Xenon',
            'Atomic Number': '54',
            'Atomic Mass': '131.29'
        },
         'Rn': {
            'Symbol': 'Rn',
            'Element': 'Radon',
            'Atomic Number': '86',
            'Atomic Mass': '222'
        }   
    }
    checkE = element in Element_list
    #Display output
    display_message = (f'Element not found', f"{Element_list.get(element, [])}")
    display(display_message[checkE], target='result')

#Linking htmls
def go_home(e):
    document.location.href = "index.html"

def go_member(e):
    document.location.href = "AddMember.html"

def go_element(e):
    document.location.href = "ElementCheck.html"

def go_creator(e):
    document.location.href = "Creator.html"

    