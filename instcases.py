#to do: 
# 1. random numbers in each line - done
# 2. other functions: couple of registers - done; extentions - done; amount - done
# 3. put only functions calls to main

#notes
# 1. exclamation mark (!) - not clear what to do from task description
# 2. imm, pimm, simm, lsb, etc. - all replaced with a number like amount
# 3. output lines can be repeated
# 4. arrays - not used

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

    # print chosen lines
    # print('unmodified lines:')
    # print(*chosenlines)
    # print('modified lines:')
    
    for x in chosenlines:
        print(remove_space_comma(select_random_extension(set_amount(remove_brackets_and_extensionword(replace_alternative_registers(replace_registers(x)))))))


        
#replace registers with recursive function      
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

#replace alternative registers with recursive function
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


def remove_brackets_and_extensionword(line):

    line = str.strip(line)

    #set of characters [], {}, ()
    brackets_pattern = r'[\([{})\]]'
    #re.sub with regex brackets_pattern
    line = re.sub(brackets_pattern,"", line)

    #remove extension words 
    extensionword_pattern = r'[a-z]*\:'
    line = re.sub(extensionword_pattern,"", line)

    #ending recursion when there is nothing more to replace
    return line


#replace amounts with recursive function
def set_amount(line):
    line = str.strip(line)
    amount_pattern = r'(\<)([a-z]+)(\>)'
    random_amount = str(random.choice(range(0,127)))

    oldlinestate = line
    line = re.sub(amount_pattern, random_amount, line)
    if line == oldlinestate:
        return line
    
    return set_amount(line)


def select_random_extension(line):
    line = str.strip(line)
    extensions_list_pattern = r'(\<)([A-Z]*[\ ]?[0-9]*[\|]?.*)(\>)'
    if not re.search(extensions_list_pattern,line):
        return line
    extensions_list = (re.search(extensions_list_pattern,line)).group(2).split('|')
    #print(extensions_list)
    
    #setting random extentions
    random_extension = str(random.choice(extensions_list))

    #re.sub with 2 regex (extentions_list_pattern and replacement)
    line = re.sub(extensions_list_pattern, random_extension, line)

    return line


def remove_space_comma(line):
    line = str.strip(line)
    space_comma_pattern = r'(\ )(\,)([\ ]?)'

    #save old line state
    oldlinestate = line
    line = re.sub(space_comma_pattern, r', ', line)
    if line == oldlinestate:
        return line

    return remove_space_comma(line)


main()