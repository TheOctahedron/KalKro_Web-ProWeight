from installer import download_programs



def delete_program(un_program):
    if un_program not in download_programs:
        print("\nGarbage Truck: Error... ")
        return {"status": "not deleted", "deleted": "none"}
    download_programs.remove(un_program)
    return {"status": "suf. deleted", "deleted": f"{un_program}"}