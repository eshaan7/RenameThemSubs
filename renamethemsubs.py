'''
Author: Eshaan Bansal
github: github.com/eshaan7

                         WHAT THE SCRIPT DOES:
	You download a TV show from torrent and find the suitable subtitle files from some website.
	Renaming every subtitle file to match the video file is a pain in the ass, isn't it?
	That's where this script comes in handyy
'''



import os

def menu():
	print("\t"+"*"*8+"MENU"+"*"*8)
	print("\n\t"+"-"*20)
	print("\t1. Same directory")
	print("\t2. Different directory")
	print("\t"+"-"*20)
	choice = int(raw_input("\n\tEnter choice(1-2): "))
	return choice

def diff_path(): #choice=2
	vid_path = str(raw_input("Full path to video directory(example: /home/...): "))
	sub_path = str(raw_input("Full path to subtitles directory(example: /home/...): "))
	sub_format = str(raw_input("Extension of subtitle file(ex: .sub, .srt, etc): "))
	vidFiles = os.listdir(vid_path)
	subFiles = os.listdir(sub_path)
	rename_files(sub_path, vidFiles, subFiles, sub_format)
	return 

def same_path(): #choice=1
	dir_path = str(raw_input("Full path to video directory(example: /home/...): "))
	dirFiles = os.listdir(dir_path)
	vid_format = str(raw_input("Extension of video file(ex: .mp4, .mkv, etc): "))
	sub_format = str(raw_input("Extension of subtitle file(ex: .sub, .srt, etc): "))
	vidFiles = []
	subFiles = []
	for name in dirFiles:
		if (name.endswith(vid_format)):
			vidFiles.append(name)
		elif (name.endswith(sub_format)):
			subFiles.append(name)
	rename_files(dir_path, vidFiles, subFiles, sub_format)
	return

def rename_files(path, vidFiles, subFiles, sub_format):
	vidFiles.sort(key=lambda f: int(filter(str.isdigit, f)))
	subFiles.sort(key=lambda f: int(filter(str.isdigit, f)))
	os.chdir(path)
	for i,vname in enumerate(vidFiles):
		print("{0} renamed to {1} ") % (subFiles[i], os.path.splitext(vname)[0])
		os.rename(subFiles[i], os.path.splitext(vname)[0]+sub_format)
	Quit = input('Press Q to Quit')
	return 

def main():
	choice = menu()
	if choice==1:
		same_path()
	elif choice==2:
		diff_path()
		
main()

