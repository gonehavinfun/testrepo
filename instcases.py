#output lines shouldn't be repeated

#import python modules
import argparse
import random
import re
from random import sample

#set variables
randomreg = random.choice(range(1,30))
#randomreg = str(randomreg)
regpattern = '[X]m> '
replacement = str(randomreg) + " "

#create arguments parser
parser = argparse.ArgumentParser("instcases.py")
parser.add_argument("casesamount", help="write number of test cases required", type=int)
args = parser.parse_args()
stringsamount = args.casesamount


#open and read file
#with open('instrs.lst') as filevar:
with open('limitedcases.lst') as filevar:
    list = filevar.readlines()
filevar.closed
#print(read_data)
#stringsamount =

#random choices of strings
resultlines = "".join(random.choices(list, k=stringsamount))
resultlines = str(resultlines)

#print chosen lines and required amount of strings
print(randomreg)
print(resultlines)

#search and replacements
subresult = re.sub(regpattern, replacement, resultlines)
print(subresult)
