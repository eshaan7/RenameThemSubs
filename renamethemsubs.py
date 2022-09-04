#!/usr/bin/env python3

'''
Author: Eshaan Bansal
github: github.com/eshaan7

						 WHAT THE SCRIPT DOES:
	You download a TV show from torrent and find the suitable subtitle files from some website.
	Renaming every subtitle file to match the video file is a pain in the ass, isn't it?
	That's where this script comes in handyy
'''

import os
import re
#import msvcrt

def menu():
	print("\t"+"*"*8+"MENU"+"*"*8)
	print("\n\t"+"-"*20)
	print("\tFor subs and video files,")
	print("\t1. In same directory")
	print("\t2. In different directory")
	print("\t3. In current directory: {0}".format(os.getcwd()))
	print("\t"+"-"*20)
	choice = int(input("\n\tEnter choice(1-3): "))
	return choice

def diff_path(): #choice=2
	vid_path = str(input("Full path to video directory(example: /home/...): "))
	sub_path = str(input("Full path to subtitles directory(example: /home/...): "))
	sub_format = str(input("Extension of subtitle files(ex: .sub, .srt, etc): "))
	vidFiles = []
	subFiles = []
	for name in os.listdir(vid_path):
		if (name.endswith('.mp4') or name.endswith('.mkv') or name.endswith('.avi')):
			vidFiles.append(name)
	for name in os.listdir(sub_path):
		if (name.endswith(sub_format)):
			subFiles.append(name)
	rename_files(sub_path, vidFiles, subFiles, sub_format)
	return 

def same_path(): #choice=1
	dir_path = str(input("Full path to video directory(example: /home/...): "))
	sub_format = str(input("Extension of subtitle files(ex: .sub, .srt, etc): "))
	dirFiles = os.listdir(dir_path)
	vidFiles = []
	subFiles = []
	for name in dirFiles:
		if (name.endswith('.mp4') or name.endswith('.mkv') or name.endswith('.avi')):
			vidFiles.append(name)
		elif (name.endswith(sub_format)):
			subFiles.append(name)
	rename_files(dir_path, vidFiles, subFiles, sub_format)
	return

def for_current_dir(): #choice=3
	dir_path = os.getcwd()
	dirFiles = os.listdir(dir_path)
	vidFiles = []
	subFiles = []
	sub_format = str(input("Extension of subtitle files(ex: .sub, .srt, etc): "))
	for name in dirFiles:
		if (name.endswith('.mp4') or name.endswith('.mkv') or name.endswith('.avi')):
			vidFiles.append(name)
		elif (name.endswith(sub_format)):
			subFiles.append(name)
	rename_files(dir_path, vidFiles, subFiles, sub_format)
	return

def rename_files(path, vidFiles, subFiles, sub_format):
	regex_exp = "([sS]\d{1,2}.*[eE]\d{1,2})"
	vidFiles.sort(key=lambda f: re.search(regex_exp, f)[0])
	subFiles.sort(key=lambda f: re.search(regex_exp, f)[0])
	os.chdir(path)
	try:
		assert(len(subFiles)==len(vidFiles))
		for i,vname in enumerate(vidFiles):
			print("{0} renamed to {1} ".format(subFiles[i], os.path.splitext(vname)[0]))
			os.rename(subFiles[i], os.path.splitext(vname)[0]+sub_format)
	except AssertionError:
		print(len(subFiles))
		print(len(vidFiles))
	#print("\nPress Q to Quit")
	#msvcrt.getch()
	return 

def main():
	choice = menu()
	if choice==1:
		same_path()
	elif choice==2:
		diff_path()
	elif choice==3:
		for_current_dir()
		
main()

