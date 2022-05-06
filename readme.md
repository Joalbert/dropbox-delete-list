This basic cli is intended to be used to list files and directories in an dropbox which you have an access key as well as delete files in some specific route, the files to be deleted will be the ones that are not included in csv file your provide.

The first column should be the route of the file and the first row is the header.

The required arguments are:
-f --file: file which contains the files that are intended to be kept in dropbox.
-p --path: the location where you are intended to clean with your file.
-k --key: your api token provided by Dropbox
Action arguments
They are mutually exclusive, it means you should use only one each time.
-l --list: list of files/directories in the path
-r --remove: remove files in the path and keep only the one listed in file.

At first, this basic cli is intended to be used to delete files that are not longer required in specific routes.
