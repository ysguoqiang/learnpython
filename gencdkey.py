# encoding:utf-8

import random
import string

class cdkeygenerator:
	def __init__(self):
		self.keyset=set()
		self.chars="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		pass
	
	def gencdkey(self,count,length):
		while count>0:
			key=''.join([random.choice(self.chars) for i in range(length)])
			if key not in self.keyset:
				count=count-1
				self.keyset.add(key)

		return self.keyset

	def setchars(self,chars):
		self.chars=chars
