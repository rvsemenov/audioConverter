#!/usr/bin/python
#coding: utf-8

import os, sys, multiprocessing
from datetime import datetime
##############################################################################################

#ffmpeg out.mp3 -i in.m4a -acodec libmp3lame -qscale:a 1
#ffmpeg -i alac.m4a -vn -acodec libfaac -aq 400 aac.m4a
##############################################################################################
def convert(root, fname, curdir):

	
	if fname[0] == '.':
		return

	print 'fname:' + fname + '\n\t',
	print '='*100+'\n\t'
	format = root[root.rfind('/')+1:]
	if len(format) < 3:
		return

	name = os.path.join(curdir, root, fname)
	print 'name:' + name + '\n\t',
	print 'format:' + format + '\n\t',
	#name with new extention
	newname = os.path.splitext(name)[0]+'.' + format
	print 'newname:' + newname + '\n\t',
	#skip if exist
	if os.path.exists(newname): 
		print 'skip'
		return

	CONVERT_CMD = 'command not found';

	if format == "mp3":
		CONVERT_CMD = 'ffmpeg "%s" -i "%s" -acodec libmp3lame -qscale:a 1';
		cmd = CONVERT_CMD % (newname, name)
	elif format == "aac":
		CONVERT_CMD = 'afconvert  -f m4af -d aac -b 192000 "%s" -o "%s"';
		cmd = CONVERT_CMD % (name, newname)
	elif format == "flac":
		CONVERT_CMD = 'afconvert  -f flac -d flac "%s" -o "%s"';
		cmd = CONVERT_CMD % (name, newname)
#https://apple.stackexchange.com/questions/365616/what-are-the-command-line-options-for-afconvert18
#ffmpeg -i alac.m4a -vn -acodec libfaac -aq 400 aac.m4a
#ffmpeg out.mp3 -i in.m4a -acodec libmp3lame -qscale:a 1

	print cmd
	os.system(cmd)
	if os.path.exists(name):
		os.remove(name)

def main():
	startTime = datetime.now()
	

	curdir = sys.argv[1]
	processes = []
	for root, dirs, fnames in os.walk(curdir):
		for fname in fnames:
			p = multiprocessing.Process(target=convert, args=(root,fname,curdir,))
			processes.append(p)
			p.start()
			                

	for process in processes:
		process.join()

	print 'done.'
	print(datetime.now() - startTime)	

if __name__ == '__main__':
	main()
