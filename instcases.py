#to do: 
# 1. random numbers in each line - done
# 2. other functions: couple of registers - done; extentions; amount
# 3. fix unmodified lines output 
# 4. put only functions calls to main


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
    #with open('instrs.lst') as filevar:
    with open('limitedcases.lst') as filevar:
        list = filevar.readlines()
    filevar.closed

    #random choices of strings
    chosenlines = random.choices(list, k=stringsamount)

    #print chosen lines
    print('unmodified lines:')
    #print(*chosenlines, sep='\n')
    print(*chosenlines)
    print('modified lines:')
    
    for x in chosenlines:
        print(replace_extentions(replace_alternative_registers(replace_registers(x))))

        
        
def replace_registers(line):
    randomreg = str(random.choice(range(1, 30)))

    #this is all madness https://stackoverflow.com/questions/5984633/python-re-sub-group-number-after-number
    #escaping escape symbols https://skillbox.ru/media/code/regulyarnye-vyrazheniya-v-python-sintaksis-poleznye-funktsii-i-zadachi/
    
    #capture groups(), raw strings in regex r', set of characters[], number
    # of occurrences{}, zero or one occurrence?  
    regpattern = r'(<)([A-Z]{1})([a-z]{1}[0-9]?)(>)'
    #capture group number reference before number \g<number>
    replacement = r'\g<2>' + randomreg
    line = str.strip(line)

    #save old line state
    oldlinestate = line
    #re.sub with 2 regex
    line = re.sub(regpattern, replacement, line, count=1)
    #ending recursion when there is nothing more to replace 
    if line == oldlinestate:
     return line

    
    return replace_registers(line)

def replace_alternative_registers(line):
    randomreg = str(random.choice(range(1, 30)))
    capturegroup_list = [2, 5]
    random_capturegroup = str(random.choice(capturegroup_list))

    #capture groups(), raw strings in regex r', set of characters[], number
    # of occurrences{}, zero or one occurrence?  
    regpattern = r'(<)([A-Z]{1})([a-z]{1}[0-9]?)(\|)([A-Z]{1})([a-z]{1}[0-9]?)(>)'
    #capture group number reference before number \g<number>
    replacement = r'\g<' + random_capturegroup + '>' + randomreg
    line = str.strip(line)

    #save old line state
    oldlinestate = line
    #re.sub with 2 regex
    line = re.sub(regpattern, replacement, line, count=1)
    #ending recursion when there is nothing more to replace 
    if line == oldlinestate:
     return line

    
    return replace_alternative_registers(line)

def replace_extentions(line):

    line = str.strip(line)

    # of occurrences{}, zero or one occurrence? 
    #capture groups(), raw strings in regex r', set of characters[]
    extpattern = r'(\ )(\{)(\,)(\<)([a-z]*)([:]?)([A-Z|]*)(\>)' 

    #set pattern for list of extentions
    extentions_list_pattern = r'([A-Z|]*)(\>)'
    extentions_list = (re.search(extentions_list_pattern,line)).group(1).split('|')
    
    #setting random extentions
    random_extention = str(random.choice(extentions_list))

    #capture group number reference before number \g<number>
    replacement = r'\g<3> ' + random_extention

    #re.sub with 2 regex (extpattern and replacement)
    line = re.sub(extpattern, replacement, line)

    #ending recursion when there is nothing more to replace 
    return line

main()