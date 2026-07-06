#=======================================================
download_programs = [
    
]



system_programs = [
    {"id": 1, "name": "Garbage Truck"}, 
    {"id": 2, "name": "Catfish-Browser (internet)"}, 
    {"id": 3, "name": "tic-tac-toe"}, 
    {"id": 4, "name": "The Randomizer"},  
    {"id": 5, "name": "SaVeLoAd"},  
    {"id": 6, "name": "diskS"}, 
    {"id": 7, "name": "Boring Calculator"}, 
    {"id": 8, "name": "Octice Office"}, 
    {"id": 9, "name": "File Conductor"} 
]



downloadable_programs = [
    {"id": 1, "name": "Rock-Paper-Scissors", "weight": 120}, 
    {"id": 2, "name": "Marketing-Simulator", "weight": 1000},
    {"id": 3, "name": "DojDo AI", "weight": 200}
]



all_disks = [
    {"id": 1, "type": "DISK", "memory": 1000, "content": []},
    {"id": 2, "type": "DISK", "memory": 1000, "content": []}, 
    {"id": 3, "type": "DISK", "memory": 1000, "content": []}
]

#=======================================================



def show_programs(type):
    if type == "system":
        return system_programs
    elif type == "installed":
        return download_programs
    

def found_program(selected):
    found = False
    for downloadable in downloadable_programs:
        if selected == downloadable['id']:
            found = True
    if found == False:
        print("\n\nThis request was not found, please enter the correct request number.")
        return "NotFound"
    return downloadable['name'], downloadable['weight']

def install_program(program_name, program_weight):
    new_id = len(download_programs) + len(system_programs) + 1
    download_programs.append({
        "id": new_id,
        "name": program_name,
        "weight": program_weight
    })
        




def found_disks(selected):
    for disk in all_disks:
        if disk["number"] == selected:
            return disk
    return {"disk": "Error: there is no such disk ID."}


    