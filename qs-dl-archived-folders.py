# Qlik Sense Archived Log file deletion utility
# Author: Clint Carr
# Date: 28/10/2016

import os, time, sys

# enter the path to the qlik sense archived logs, default: C:\ProgramData\Qlik\Sense\Repository\Archived Logs
logpath = 'C:\\Dev\\Archived Logs'
# enter the path of the log file to log the files deleted
deletedfilelog = 'C:\\Dev\\deletedfiles'

#set the date you wish to delete from.  this value is in epoch time. time.time() - (10 * 86400) = ten days ago
cutoff = time.time() - (1 * 86400)

# loop through folders
for foldername, subfolders, filenames in os.walk(logpath):
	print foldername
# loop through subfolders
	for subfolder in subfolders:
		print foldername + '\\' + subfolder
# delete files where the creation date is less than the cutoff date
	for filename in filenames:
		x = os.stat(foldername +'\\'+ filename)
		y = x.st_mtime
		if y < cutoff:
			os.remove(foldername +'\\'+ filename)
# write the file path and name to a log
			with open(deletedfilelog, "a") as f:
				f.write(foldername +'\\'+ filename)
				f.write("\n")