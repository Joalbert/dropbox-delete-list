from helpers.helper import (format_csv, diff_files)
import sys
import os

def print_out_directory(directory:tuple)->None:
    """ print out list directory and files if any, data is passed as followed item 0 files and item 1 directories."""
    for index, item in enumerate(directory[1]):
        if index==0:
            print("DIR:",end="\n", file=sys.stdout)
            print("====", file=sys.stdout)
        print(f"--{item.name}")
    for index, item in enumerate(directory[0]):
        if index==0:
            print("FILES:",end="\n", file=sys.stdout)
            print("======", file=sys.stdout)
        print(f"--{item['name']} {item['server_modified']}",end="\n")
        if (index==len(directory[0])-1):
            print(f"Files: {len(directory[0])} items", file=sys.stdout)

def remove_files(directory:tuple, filenames_to_be_kept:"list[str]", 
                delete:'function')->None:
    """ remove files in directory that are not in filenames_to_be_kept list, 
        directory is passed as followed item 0 files and item 1 directories.
    """
    
    # a -Files to be deleted
    file_to_delete = diff_files(files_in_db=filenames_to_be_kept, 
                                files_in_server=directory[0], 
                                field_output="name")
    for item in file_to_delete:
        print(f"{item}\t{id}", sep="\n")
    print(f"Files to be deleted: {len(file_to_delete)} files.", 
         file=sys.stdout)
    confirm = input("Do you really want to delete the files listed [y/n]? \n")
    if confirm=="y":
        delete(file_to_delete)
        print(f"It has been deleted {len(file_to_delete)} files!", 
             file=sys.stdout)
    else:
        print("Deletion has been canceled!", file=sys.stdout)