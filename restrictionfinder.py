#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  restrictionfinder.py
#  
#  Copyright 2014 Gily Merkado <gilymerkado@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# read the txt files of the restriction enzymes and find the sepcific enzymes for each group.
# the groups are defined in a different csv file.
# the data is organized in an array by rows of groups (each row is a group).

import os
import csv
from pylab import *
import datetime

def read_csv_file(filename):
	'''reads a csv file and returns it as a list of rows'''
	data = []
	f = open(filename)
	cr = csv.reader(f)
	for row in cr:
		data.append(row)
	f.close()
	return data

def get_groups_names(filename):
	'''get the groups of specimens from the definitions file.
	return a list of group names.
	'''
	data = array(read_csv_file('forams_groups.csv'))
	groups = []
	for group in data:
		group_name = group[0]
		groups.append(group_name)
	return groups
			

class Group:
	'''A group of specimens with common and specific restriction enzymes.
	'''
	def __init__(self, name):
		self.name = name
		self.filename = 'filename' # The definitions file (csv)
	
	def read_txt_file(self, filename):
		'''reads a txt file and returns it as a list of rows'''
		rows = []
		f = open(filename, 'r')
		for row in f:
			rows.append(row)
		f.close()
		return rows
	
	def get_specimens(self, filename):
		'''get the list of specimens in the group.
		filname - string, name of definitions file.
		return a list of specimens.
		'''
		data = array(read_csv_file(filename))
		specimens = []
		for group in data:
			for specimen in group[1:]:
				specimens.append(specimen)
		return specimens
	
	def get_enzymes(self, specimens):
		'''return a dictionary of specimen:enzymes'''
		enzymes_dict = dict()
		for specimen in specimens:
			if specimen != '': # There is another specimen to be checked
				filename = specimen + '.txt'
				f = './NEB/' + filename
				r = self.read_txt_file(f) # read the text file of the specimen
				# get the enzymes names in a list
				enzyme = []
				for  i in range(3, len(r)-1, 3):
					enzymes.append(r[i])
				enzymes_dict[specimen] = enzymes
		return enzymes_dict

	def get_common_enzymes(self):
		'''return a list of the common enzymes to the whole group.
		specimens - a dictionary of the specimens and thier enzymes
		'''
		common_enzymes = set()
		all_enzymes = set()
		specimens = get_specimens(self, self.filename) # list
		specimens_enzymes = get_enzymes(self, specimens) # dictionay specimen:[enzymes]
		all_enzymes_lists = specimens_enzymes.values() # create a list of lists of enzymes
		for enzymes_list in all_enzymes_lists:
			if type(enzymes_list) == list:
				for enzyme in enzyme_list:
					all_enzymes.add(enzyme)
					flag = True # a flag that indicates that the enzyme exists in all specimens
					while flag:
						for specimen in specimens:
							if enzyme not in specimens_enzymes[specimen]:
								flag = False
						break
					if flag:
						common_enzymes.add(enzyme)
			else:
				flag = True # a flag that indicates that the enzyme exists in all specimens
				while flag:
					for specimen in specimens:
						if enzymes_list not in specimens_enzymes[specimen]:
							flag = False
							break
				if flag:
					common_enzymes.add(enzyme_list)
		return common_enzymes
		
	def get_specific_enzymes(listOfCommonEnzymes, listOfCommonFromOtherGroup):
		'''return a list of the specific enzymes when compared with 
		another group.
		input - A list of the common enzymes of the group.
		A list of the common enzymes of the group to be compared with.
		'''
		specific_enzymes = []
		for enzyme in listOfCommonEnzymes:
			if enzyme not in listOfCommonFromOtherGroup:
				specific_enzymes.append(enzyme)
		return specific_enzymes
		
		
def main():
	
	return 0

if __name__ == '__main__':
	main()

