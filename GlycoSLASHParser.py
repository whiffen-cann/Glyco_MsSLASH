#!/usr/bin/env python3
from sys import argv
from os import listdir
from os.path import isfile, join
import glob

filedir = argv[1]
files = glob.glob(filedir+"/"+"*.GlycoSLASH.tsv")

spectralID = 0
spectralDict = dict()
uniqueID = dict()
uniqueGlycoID = dict()
for filename in files:
	#print filename
	tmp = filename+".uniqueID"
	tmpfile = open(tmp,'w')
	eachAllele = dict()
	eachSpectra = 0
	eachSpectraID = 0
	with open(filename) as f:
		next(f)
		for line in f:
			if 'TopScore' in line:
				continue
			eachSpectra += 1
			line = line.rstrip()
			lines = line.split('\t')
			topscore = float(lines[4])
			#print topscore
			topPep = lines[5]
			topSpectra = lines[1]
			libs = lines[5].split('_')
			lib = ""
			if len(libs) >= 4:
				lib = libs[0]+"_"+libs[1]
			else:
				lib = libs[0]
			if topscore >= 0.6:
				eachSpectraID += 1
				spectralID += 1
				uniqueID[topPep] = 1
				if '[' in topPep :
					uniqueGlycoID[topPep] = 1
				spectralDict[topSpectra] = 1
				if topPep in eachAllele:
					eachAllele[topPep] += 1
				else:
					eachAllele[topPep] = 1
	for each in eachAllele:
		tmpfile.write(each+"	"+str(eachAllele[each])+"\n")
	tmpfile.close()
	tmps = filename.split('/')
	filename = tmps[len(tmps)-1]
	print ("Filename\tUniqueID\tTotal Spectra\tSpectra ID number\tRatio of ID")
	print (filename,'\t',len(eachAllele),'\t',eachSpectra,'\t',eachSpectraID,'\t',float(eachSpectraID)/eachSpectra)
			#print line

print (len(uniqueID))
print (len(spectralDict))
print (len(uniqueGlycoID))
#print 'the total number is '+str(spectralID)
