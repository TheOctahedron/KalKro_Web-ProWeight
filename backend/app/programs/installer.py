installed_programs = []


system_programs = [
    {"id": 1, "name": "Garbage Truck"},
    {"id": 2, "name": "Settings"},
    {"id": 3, "name": "Internet"},
    {"id": 4, "name": "tic tac toe"},
    {"id": 5, "name": "The randomizer"},
    {"id": 6, "name": "SaVeLoAd"},
    {"id": 7, "name": "discS"},
    {"id": 8, "name": "Boring Calculator"},
    {"id": 9, "name": "Octice Office"}
] 


all_discs = [
    {"number": 1, "memory": 1000},
    {"number": 2, "memory": 1000},
    {"number": 3, "memory": 1000}
]





def show_programs(type):
    if type == "system":
        return system_programs
    elif type == "installed":
        return installed_programs
    



def install_program(program_name, program_weight):
    for program, weight in installed_programs:
        if program_name == program:
            print("\nSorry, but you already have this program.")
            pass




def found_discs(selected):
    for disc in all_discs:
        if disc["number"] == selected:
            return disc
    return {"disc": "Error: there is no such disc ID."}
    