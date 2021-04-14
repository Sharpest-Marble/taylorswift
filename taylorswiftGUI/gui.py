from taylorswift import PACKAGEDIR as taypackage
import numpy as np
import tkinter as tk
import csv, os

def setup():
	# load the data
	data = []
	with open(os.path.join(taypackage,'Grades.csv'),'rt') as f:
		data=[row for row in csv.reader(f,delimiter=',')]
	
	#initialize
	numsongs=149

	title=[0]*numsongs
	album=[0]*numsongs
	allhappy=np.zeros(numsongs)
	alldate=np.zeros(numsongs)
	selffeel=np.zeros(numsongs)
	glassfull=np.zeros(numsongs)
	stages=np.zeros(numsongs)
	tempo=np.zeros(numsongs)
	seriousness=np.zeros(numsongs)
	future=np.zeros(numsongs)
	malefeel=np.zeros(numsongs)
	together=np.zeros(numsongs)
	
	i=0
	for number in range(2,numsongs+2):
		set=data[number]
		title[i]=set[0]
		album[i]=set[1]
		allhappy[i]=float(set[2])
		alldate[i]=float(set[3])
		selffeel[i]=float(set[4])
		glassfull[i]=float(set[5])
		stages[i]=float(set[6])
		tempo[i]=float(set[7])
		seriousness[i]=float(set[8])
		future[i]=float(set[9])
		malefeel[i]=float(set[10])
		together[i]=float(set[11])
		i+=1

	texts=np.loadtxt(os.path.join(taypackage, 'answertext.txt'),delimiter='#',dtype='str')

setup()