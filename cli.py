import argparse
import sys
from requests.exceptions import ConnectionError

from helpers.helper import Connection, format_csv
from commands import print_out_directory, remove_files

def parse_arguments():
    parser = argparse.ArgumentParser(prog="Cleaned directory in Dropbox.")
    parser.add_argument("-f", "--file", help="File with existant files in database", required=True)
    parser.add_argument("-p", "--path", help="directory to be shown/cleaned in Dropbox", required=True)
    parser.add_argument("-k", "--key", help="API Token in Dropbox", required=True)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--list", help="Show files", action="store_true")
    group.add_argument("-r", "--remove", help="Delete files", action="store_true")
    return parser.parse_args()

def main():
    # 1 - Define Arg parser
    args = parse_arguments()
    
    # 2 - Initiate connection to Dropbox and getting files in server 
    connection =Connection(args.key)
    try:
        directory = connection.get_files(path=args.path)
    except ConnectionError:
        print("Please, try later", file=sys.stdout)
        return 1

    if args.list:
        try:
            print_out_directory(directory)
            return 0
        except ConnectionError:
            print("Please, try later", file=sys.stdout)

    # 3 - Remove files
    if args.remove:
        try:
            remove_files(directory=directory, filenames_to_be_kept=format_csv(args.file), delete=connection.delete_files)
        except ConnectionError:
            print("Please, try later", file=sys.stdout)
        return 0

if __name__ == "__main__":
    exit(main())        
            