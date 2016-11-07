import os,sys # Importing necessary libraries

for root, dirs, files in os.walk("."): # Use os.walk to walk through all files and directories within the enclosing directory
	for name in files:
		#print(os.path.join(root,name))
		s=os.path.join(root,name) # Concatenate root directory and filename into string
		if name.endswith(".fastq"): # If the file ends with .fastq ...
			t=s.split('/') # Split t on '/' to index individual chunks of the array
			v=t[1].split('-') # Split v on '-' to index individual chunks of the array
			print('./fastq/'+v[0]+'.fastq')
			#os.rename(root+'/'+name,'./fastq/'+v[0]+'.fastq') # rename file from local path + name to the name of the parent directory + .fasta