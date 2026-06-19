from fastapi import APIRouter
from programs.installer import show_programs, install_program, all_discs, found_discs
from datas.users import new_user

router = APIRouter()



@router.get("/system/desktop/allprograms/{type}") #
def show_myprograms(type: str):
    return show_programs(type)




@router.post("/start/{new_username}") #
def create_user(new_username: str):
    username = new_user(new_username)
    return {"Go": f"User: {username}"}




@router.post("/system/installer/install_program/{program_name}/{program_weight}") #
def download_program(program_name: str, program_weight: int):
    return install_program(program_name, program_weight)
    




@router.get("/system/installer/show_discs") #
def show_mydiscs():
    return all_discs




@router.get("/system/installer/mydiscs/{selected}") # 
def select_discs(selected: int):
    return found_discs(selected)