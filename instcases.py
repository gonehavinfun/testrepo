#to do: 
# 1. random numbers in each line
# 2. other functions: couple of registers, extentions, amount
# 3. fix join


#output lines can be repeated

#import python modules
import argparse
import random
import re
from random import sample

def main():
    #create arguments parser
    parser = argparse.ArgumentParser("instcases.py")
    parser.add_argument("casesamount", help="write number of test cases required", type=int)
    args = parser.parse_args()
    stringsamount = args.casesamount

    #open and read file
    with open('instrs.lst') as filevar:
    #with open('limitedcases.lst') as filevar:
        list = filevar.readlines()
    filevar.closed

    #random choices of strings
    chosenlines = random.choices(list, k=stringsamount)
    resultlines = "".join(chosenlines)
    resultlines = str(resultlines)

    #print chosen lines
    print('unmodified lines:\n' + resultlines)
    print('modified lines:')
    for x in chosenlines:
        print(function2(function1(x)))
        


def function1(line):
    randomreg = str(random.choice(range(1,30)))

    #this is all madness https://stackoverflow.com/questions/5984633/python-re-sub-group-number-after-number
    #escaping escape symbols https://skillbox.ru/media/code/regulyarnye-vyrazheniya-v-python-sintaksis-poleznye-funktsii-i-zadachi/
    
    #capture groups(), raw strings in regex r', set of characters[], number
    # of occurrences{}, zero or one occurrence?  
    regpattern = r'(<)([A-Z]{1})([a-z]{1}[0-9]?>)'
    #capture group number reference before number \g<number>
    replacement = r'\g<2>' + randomreg
    line = str.strip(line)
    #re.sub with 2 regex
    line = re.sub(regpattern, replacement, line)
    return line

def function2(line):
    line = line + ' +2'
    return line

main()