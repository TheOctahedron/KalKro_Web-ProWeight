# WEB 
from fastapi import APIRouter
# ===========================
# APPS
from programs.apps.installer import show_programs, install_program, all_disks, found_disks, found_program
from programs.apps.boring_calculator import boring_plus, boring_minus, boring_division, boring_multiplication, boring_absurdabsurd
from programs.apps.randomizer import random_number
from programs.apps.garbage_truck import delete_program
# ===========================
# USERS DATA
from datas.users import new_user
# ===========================

router = APIRouter()



@router.get("/system/files/{type}")  # shows programs based on type
def show_my_programs(type: str):
    return show_programs(type)




@router.post("/start/{new_username}")  # creates a new user
def create_user(new_username: str):
    username = new_user(new_username)
    return {"Go": f"User: {username}"}




@router.post("/system/installer/install_program/{program_name}/{program_weight}")  # downloads programs
def install_my_program(program_name: str, program_weight: int):
    return install_program(program_name, program_weight)




@router.get("/system/installer/found_program/{program_id}")  # finds a program by ID 
def found_my_program(program_id: int):
    return found_program(program_id)




@router.get("/system/installer/disks/show_all")  # shows all disks
def show_my_discs():
    return all_disks




@router.get("/system/installer/disks/select/{selected}")  # selects a disk
def found_my_discs(selected: int):
    return found_disks(selected)




@router.delete("/system/garbage_truck/{un_program}")  # delete a program by ID
def delete_my_program(un_program: int):
    return delete_program(un_program)




# ================================== APPS ==================================

# Randomizer
@router.get("/system/randomizer/random/{number}")  # Gives a random number from 1 to the selected one.
def my_random_number(number: int):
    return random_number(number)
# ==========




# B-Calculator
@router.get("/system/b_calculator/plus/{numbers}") # PLUS
def my_boring_plus(numbers: int):
    return boring_plus(numbers) 


@router.get("/system/b_calculator/minus/{numbers}") # MINUS
def my_boring_minus(numbers: int):
    return boring_minus(numbers) 


@router.get("/system/b_calculator/division/{numbers}") # DIVISON
def my_boring_division(numbers: int):
    return boring_division(numbers) 


@router.get("/system/b_calculator/multiplication/{numbers}") # MULTIPLICATION 
def my_boring_multiplication(numbers: int):
    return boring_multiplication(numbers) 


@router.get("/system/b_calculator/absurdabsurd/{numbers}") # ABSURDABSURD
def my_boring_absurdabsurd(numbers: int):
    return boring_absurdabsurd(numbers) 
# ==========

