<h1>Purpose</h1>
<p>
This basic cli is intended to be used to list files and directories in an dropbox which you have an access key as well as delete files in some specific route, the files to be deleted will be the ones 
that are not included in csv file your provide.
</p>
<p>
At first, this basic cli is intended to be used to delete files that are not longer required in specific routes.
</p>

<h1>How it works</h1>
<p>
The first column should be the route of the file and the first row is the header.
</p>
<h2>Arguments</h2>
<p>
<h3>Required Arguments</h3> 
</p> 
<table>
<thead>
<th>Flags</th>
<th>Flags long</th>
<th>Function</th>
</thead>
<tr>
<td>-f</td>
<td>--file</td>
<td>File which contains the files that are intended to be kept in dropbox.</td>
</tr>
<tr>
<td>-k</td>
<td>--key</td>
<td>Your api token provided by Dropbox.</td>
</tr>
</table>
<h3>Action arguments</h3>   
They are two flgs that are mutually exclusive, it means you should use only one each time. 

<table>
<thead>
<th>Flags</th>
<th>Flags long</th>
<th>Function</th>
</thead>
<tr>
<td>-l</td>
<td>--list</td>
<td>List of files/directories in the path</td>
</tr>
<tr>
<td>-r</td>
<td>--remove</td>
<td>Remove files in the path and keep only the one listed in file.</td>
</tr>
<tr>
<td>-p</td>
<td>--path</td>
<td>The location where you are intended to clean with your file.Only should be used with -r argument.
</td>
</tr>
</table>
 
<h1>Examples</h1>
<h3> List Files from a directory in Dropbox</h3>
<code> python3 cli.py -k $TOKEN -p "" -l </code>
<h4>Output:</h4>
<p>DIR:</p>
<p>====</p>
<p>--app</p>
<p>--media</p>
<p>--home</p>
<p>FILES:</p>
<p>======</p>
<p>--256x256.svg 2021-11-01 19:47:59</p>
<p>--64x64.svg 2021-11-01 19:47:59</p>
<p>Files: 2 items</p>

<h3> List Files from a directory which is empty in Dropbox</h3>
<code>python3 cli.py -k $TOKEN -p "/app/media/identifications/images" -l</code>
<h4>Output:</h4>
<p>It is empty.</p>

<h3> Try to delete files but you cancel when the prompt ask for confirmation </h3>
<code>python3 cli.py -k $TOKEN -p "/home/joalbert/Documents/test/dummy/media/country/images" -r -f data/payment_db.csv</code>
<h4>Output:</h4>
<p>/home/joalbert/Documents/test/dummy/media/country/images/us.png</p>
<p>/home/joalbert/Documents/test/dummy/media/country/images/us_bP4iy1J.png</p>
<p>/home/joalbert/Documents/test/dummy/media/country/images/us_RqUcRG3.png</p>
<p>Files to be deleted: 3 files.</p>
<p>Do you really want to delete the files listed [y/n]?
n</p>
<p>Deletion has been canceled!</p>

<h3> Try to delete files and you confirm when the prompt ask for confirmation </h3>
<code>python3 cli.py -k $TOKEN -p "/home/joalbert/Documents/test/dummy/media/country/images" -r -f data/payment_db.csv</code>
<p>/home/joalbert/Documents/test/dummy/media/country/images/us.png</p>
<p>/home/joalbert/Documents/test/dummy/media/country/images/us_bP4iy1J.png</p>
<p>/home/joalbert/Documents/test/dummy/media/country/images/us_RqUcRG3.png</p>
<p>Files to be deleted: 3 files.</p>
<p>Do you really want to delete the files listed [y/n]?
y</p>
<p>File: /home/joalbert/Documents/test/dummy/media/country/images/us.png was successfully deleted!</p>
<p>File: /home/joalbert/Documents/test/dummy/media/country/images/us_bP4iy1J.png was successfully deleted!</p>
<p>File: /home/joalbert/Documents/test/dummy/media/country/images/us_RqUcRG3.png was successfully deleted!</p>
<p>It has been deleted 3 files!</p>

