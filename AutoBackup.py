#
#					AutoBackup.py - 0.1
#
#
#	Copyright 2017 Christopher Ribeiro
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.



# Import the needed modules;
from time import sleep as Sleep;
from distutils.dir_util import copy_tree as Copy;
from sys import argv as Arguments;


# Main class;
class AutoBackup ():
	# Instantiate the class;
	#
	# MainFolder: String;
	# TargetFolder: String;
	# Delay: String;
	def __init__ (self, MainFolder, TargetFolder, Delay):
		# Set the folder to be copied by the MainFolder argument;
		self.MainFolder = MainFolder;

		# Set the destination folder by the TargetFolder argument;
		self.TargetFolder = TargetFolder;

		# Set the interval to save the folder;
		self.Delay = Delay;

		# Start the whole process;
		self.Backup ();


	# Backup the especified files;
	def Backup (self):
		# Main loop, trying to copy from one directory to another;
		while True:
			# Try copy files from MainFolder to TargetFolder;
			try:
				Copy (self.MainFolder, self.TargetFolder);
			except:
				# If can't copy, tell the user and stop the process;
				print ("Could Not Execute The Backup.");
				break;

			# Tell the user that the backup has been done;
			print ("Backup Done!\n Files Copied From: %s To: %s." % (self.MainFolder, self.TargetFolder));

			# Wait using the Delay before save again;
			Sleep (int (self.Delay));



# Start the backup process at file execution;
if __name__ == "__main__":
	# Check if the received arguments was 3;
	if len (Arguments)  > 4 or len (Arguments) < 4:
		# Prompt the user with the correct arguments to be used;
		print ("Argument Must Be:\nAutoBackup ConfigFile");
	else:
		# Start the AutoBackup class by the given arguments;
		AutoBackup (Arguments[1], Arguments[2], Arguments[3]);
