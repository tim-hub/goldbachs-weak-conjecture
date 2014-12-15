#!/usr/bin/env python
# -*- coding: utf-8 -*-

#def main():

	#return 0

#if __name__ == '__main__':
	#main()
Max=1000
Max=int(raw_input('Firstly, input a max number to prove the three odds:\n'))
#use 1000 to test


#get the number list
def findPrimeNumberList(stop=1000,start=3):
	primeNumberList=[1,2,]
	for i in range(start,stop+1):
		if testPrimeNumber(i):
			primeNumberList.append(i)
	return primeNumberList

# test the number x is or not is a prime number
def testPrimeNumber(x):
	for i in range(2,x):
		if x%i==0:
			return False
	return True
		

# verify the conjecture is or not is right
def verifyConjecture(pNumberList):

	for i in range(9,Max+1,2):
		print(verifying(i,pNumberList))
		


#verify i number obey the conjecture or not
def verifying(i,pNumberList):
	for j in pNumberList:
			for k in pNumberList:
				for l in pNumberList:
					if i ==j+k+l:
						return('%d=%d+%d+%d, Conjecture on number %i is true') %(i,j,k,l,i)
	return 'The conjecture is wrong!!!'



primeNumberList=(findPrimeNumberList(Max))

print(' from 1 to %d, all prime numbers are in the list:') %Max
print(primeNumberList)

primeNumberList.pop(1)
verifyConjecture(primeNumberList)