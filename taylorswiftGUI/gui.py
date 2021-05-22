import csv
import os
from tkinter import Tk,IntVar,N,W,E,S
from tkinter import ttk

import numpy as np
from taylorswift import PACKAGEDIR as taypackagedir


class taylorswiftGUI:
	def __init__(self):
		# load the data
		self.data = []
		with open(os.path.join(taypackagedir,'Grades.csv'),'rt') as f:
			self.data=[row for row in csv.reader(f,delimiter=',')]
		
		#initialize
		# this is for the gui
		self.root = Tk()

		self.numsongs=149
		#relationship vector + happiness vector
		self.relhap = [IntVar(self.root)]*7

		self.title=[0]*self.numsongs
		self.album=[0]*self.numsongs
		self.allhappy=np.zeros(self.numsongs)
		self.alldate=np.zeros(self.numsongs)
		self.selffeel=np.zeros(self.numsongs)
		self.glassfull=np.zeros(self.numsongs)
		self.stages=np.zeros(self.numsongs)
		self.tempo=np.zeros(self.numsongs)
		self.seriousness=np.zeros(self.numsongs)
		self.future=np.zeros(self.numsongs)
		self.malefeel=np.zeros(self.numsongs)
		self.together=np.zeros(self.numsongs)
		
		i=0
		for number in range(2,self.numsongs+2):
			self.set=self.data[number]
			self.title[i]=self.set[0]
			self.album[i]=self.set[1]
			self.allhappy[i]=float(self.set[2])
			self.alldate[i]=float(self.set[3])
			self.selffeel[i]=float(self.set[4])
			self.glassfull[i]=float(self.set[5])
			self.stages[i]=float(self.set[6])
			self.tempo[i]=float(self.set[7])
			self.seriousness[i]=float(self.set[8])
			self.future[i]=float(self.set[9])
			self.malefeel[i]=float(self.set[10])
			self.together[i]=float(self.set[11])
			i+=1
		# the answers for taytaysongs
		self.texts=np.loadtxt(os.path.join(taypackagedir, 'answertext.txt'),delimiter='#',dtype='str')
		# initialize the final list to empty
		self.finalok = [] 

	# grabs user input for the questions and stores it
	def ask_questions(self):
		answers = [
		[
			"Our relationship ended because of cataclysmic past offenses. OR Our relationship has some serious problems."
			"My feelings were a bit hurt when our relationship ended. OR Our relationship is going ok but has some problems.",
			"Our relationship ended, but not in a horribly bad way. It just ended. OR I feel pretty mediocre about the quality of our relationship.",
			"I wish I was in a relationship, but I don't think it will happen right now. OR I'm happy without a relationship right now.",
			"My relationship is pretty casual at the moment, not official or anything. OR I look back fondly on my past relationship, without feeling hurt or angry.",
			"My relationship is going well and we're thinking about long-term commitment.",
			"I'm getting married and/or comitting to this relationship for the rest of my life."],
		[
			"We're never speaking again.",
			"We're probably going to see each other again at some point, but we won't be in touch much at all.",
			"We might talk a bit less than we did in the past.",
			"I'm not sure what our future is.",
			"We've got some casual future plans but nothing serious lined up. OR We might hang out but I'm not sure.",
			"We're going to be spending a fair amount of time together in the future.",
			"We're going to be spending a large amount of time together. Like maybe getting married."],
		[
			"They've told me they hate me.",
			"I think they don't like me that much. OR They've insulted me some.",
			"They're nice to me but they see me as just a friend.",
			"I'm not sure and/or they haven't made it clear to me.",
			"They maybe have some non-platonic feelings for me but I'm not sure how strong they are.",
			"They've told me that they have some feelings for me.",
			"They have openly declared their love for me to the world."
		],
		[
			"There are significant barriers that prevent us from being together.",
			"There aren't any insurmountable barriers between us, but we never do anything together.",
			"We do some things together but spend most of our time doing things alone.",
			"We do about the same amount of stuff together as we do alone.",
			"We do some things alone but spend most of our time doing things together.",
			"We do pretty much everything together.",
			"We do everything together, and even when we aren't together I only think about us being together."
		],
		[
			"I have a lot of problems and they're all my fault.",
			"I have a lot of problems, but I don't think they're all my fault.",
			"I don't have a ton of significant problems, but sometimes I think I could do better.",
			"I'm not really sure how I feel.",
			"I feel pretty good about myself, and am just a little insecure on occasion.",
			"I have a few concerns but feel very good overall.",
			"I'm awesome, my life is awesome, this is the bomb."
		],
		[
			"You're really angry about something and/or really depressed about something.",
			"You don't like how your life is going and you just want to make a deal to get your old life back.",
			"You know something's wrong with your life but you want to ignore it.",
			"You've accepted the bad things that have happened to you and are ready to move on from them.",
			"You're feeling pretty neutral and you're waiting for life to make you happy.",
			"You're actively working to make yourself happy.",
			"You're actively working to make yourself happy and trying to make sure that everyone else is happy too."
		]
		]

		# # prolly gonna need to scrap this whole thing

		# label_make = lambda iter: [ttk.Label(self.root) for i in range(iter)]
		# label_grider = lambda label,iter: [label[j].grid(column=0,row=1+j*2,sticky='we') for j in range(iter)]
		# def label_follower(label,iter):
		# 	for i in range(iter):
		# 		label[i].configure(textvariable=self.relhap[i].get())
		# # label.grid(column=0,row=1+i*2,sticky='we')
		# # def update_lbl(val): 
		# 	# labels[i]['text'] = answers[i][int(val)]
		# def q_make(iter):
		# 	return [ttk.Scale(self.root,orient='horizontal', length=1000, from_=1,to=7,variable=self.relhap[i]) for i in range(iter)]
		# def q_grid(q,iter):
		# 	for i in range(iter):
		# 		q[i].grid(column=0,row=2+2*i, sticky='we')
		# 		q[i].set(4)
		# q = q_make(6)
		# q_grid(q,6)
		# label = label_make(6)
		# label_grider(label,6)
		# label_follower(label,6)
		# # q[0].grid(column=0, row=2, sticky='we')
		# # q.set(4)
	
		# answer_labels = [answer_label_gen(i) for i in range(7)]
		# print(answer_labels[0])
		# def update_lbl(val):
			# print(int(val))
			# answer_labels[i]['text'] = answers[i][int(self.relhap[i])]
		
		# self.rel[0] = int(q1)
		# self.rel[0] = int(input("enter a number from 1-7: "))-4
		# self.rel[1] = int(input("enter a number from 1-7: "))-4
		# self.rel[2] = int(input("enter a number from 1-7: "))-4
		# self.rel[3] = int(input("enter a number from 1-7: "))-4
		# self.hap[0] = int(input("enter a number from 1-7:"))-4
		# self.hap[1] = int(input("enter a number from 1-7:"))-4

	# calculates the perfect song based on the prior answers
	def calculate_song(self):
		rel = self.relhap[0:-2]
		hap = self.relhap[-2:-1]
		# calculates each song's distance from the answer
		selferr=np.array([self.selffeel[i]-rel[0].get() for i in range(0,self.numsongs)])
		stageserr=np.array([self.stages[i]-rel[1].get() for i in range(0,self.numsongs)])
		seriouserr=np.array([self.seriousness[i]-rel[2].get() for i in range(0,self.numsongs)])
		futureerr=np.array([self.future[i]-rel[3].get() for i in range(0,self.numsongs)])
		maleerr=np.array([self.malefeel[i]-hap[0].get() for i in range(0,self.numsongs)])
		togethererr=np.array([self.together[i]-hap[1].get() for i in range(0,self.numsongs)])
		
		# seems to be the total distance from answer to song, or net error
		neterr=np.zeros(self.numsongs)
		for _ in range(0,self.numsongs):
			neterr=selferr**2.+stageserr**2.+seriouserr**2.+futureerr**2.+maleerr**2.+togethererr**2.
		
		# list of songs where the error is between zero and 40, in order of error
		oklist=np.zeros(20)
		index=0
		n=0
		# refactored slightly to have clearer loop controls
		while n < 40 and index<5:
			if any(np.abs(neterr)==n):
				ok=np.where(np.abs(neterr)==n)[0]
				for x in ok:
					oklist[index]=x
					index+=1
			n+=1
		okintlist=[int(i) for i in oklist]
		self.finalok=okintlist[0:5]
	# compile the songs into a list, and print them (in test)
	def list_songs(self):
		for x,item in enumerate(self.finalok):
			n=x+1
			print(str(n)+': '+self.title[item])
			print(self.texts[item])
	# basically the original version but this time it's in an oop format
	def print_test(self):
		self.ask_questions()
		self.calculate_song()
		self.list_songs()

	# actually displays the gui
	def display_framework_gui(self):
		# draw the window basically
		self.root.title("Taylor Swift Mood Meter")
		mainframe = ttk.Frame(self.root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		self.root.columnconfigure(0, weight=1)
		self.root.rowconfigure(0, weight=1)
		self.ask_questions()
		self.root.mainloop()


tay = taylorswiftGUI()
tay.display_framework_gui()
