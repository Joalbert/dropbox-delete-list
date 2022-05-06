This basic cli is intended to be used to list files and directories in an dropbox which you have an access key as well as delete files in some specific route, the files to be deleted will be the ones that are not included in csv file your provide.

The first column should be the route of the file and the first row is the header.

The required arguments are: 
-f --file: file which contains the files that are intended to be kept in dropbox. 
-k --key: your api token provided by Dropbox.

Action arguments 
They are mutually exclusive, it means you should use only one each time. 
-l --list: list of files/directories in the path 
-r --remove: remove files in the path and keep only the one listed in file.

if you use -r argument then you should complete path argument.
-p --path: the location where you are intended to clean with your file. 

At first, this basic cli is intended to be used to delete files that are not longer required in specific routes.

Examples:
>> python3 cli.py -k $TOKEN -p "" -l
DIR:
====
--app
--media
--home
FILES:
======
--256x256.svg 2021-11-01 19:47:59
--64x64.svg 2021-11-01 19:47:59
Files: 2 items

>> python3 cli.py -k $TOKEN -p "/app/media/identifications/images" -l
It is empty.

>> python3 cli.py -k $TOKEN -p "/home/joalbert/Documents/test/dummy/media/country/images" -r -f data/payment_db.csv
/home/joalbert/Documents/test/dummy/media/country/images/us.png
/home/joalbert/Documents/test/dummy/media/country/images/us_bP4iy1J.png
/home/joalbert/Documents/test/dummy/media/country/images/us_RqUcRG3.png
Files to be deleted: 3 files.
Do you really want to delete the files listed [y/n]?
n
Deletion has been canceled!

>> python3 cli.py -k $TOKEN -p "/home/joalbert/Documents/test/dummy/media/country/images" -r -f data/payment_db.csv
/home/joalbert/Documents/test/dummy/media/country/images/us.png
/home/joalbert/Documents/test/dummy/media/country/images/us_bP4iy1J.png
/home/joalbert/Documents/test/dummy/media/country/images/us_RqUcRG3.png
Files to be deleted: 3 files.
Do you really want to delete the files listed [y/n]?
y
File: /home/joalbert/Documents/test/dummy/media/country/images/us.png was successfully deleted!
File: /home/joalbert/Documents/test/dummy/media/country/images/us_bP4iy1J.png was successfully deleted!
File: /home/joalbert/Documents/test/dummy/media/country/images/us_RqUcRG3.png was successfully deleted!
It has been deleted 3 files!

