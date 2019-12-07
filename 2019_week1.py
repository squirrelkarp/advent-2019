#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Day 1, part 1

with open(r'C:\Users\david\Documents\advent_of_code\input1_1.txt','r') as infile:
    l = [int(line) for line in infile.readlines()]
    

fuel = [max(0,mass//3 - 2) for mass in l]
print(sum(fuel))

#Day 1, part 2
total_fuel = sum(fuel)
while sum(fuel) > 0:
    fuel = [max(0,mass//3 - 2) for mass in fuel]
    total_fuel += sum(fuel)

print(total_fuel)


# In[34]:


# Day 2, part 1

import csv
import copy

def run_intcode(intcode):
    mem=copy.copy(intcode)
    i=0
    while i < len(mem):
        if mem[i] == 1:
            mem[mem[i+3]]=mem[mem[i+1]]+mem[mem[i+2]]
            i+=4
        elif mem[i] == 2:
            mem[mem[i+3]]=mem[mem[i+1]]*mem[mem[i+2]]
            i+=4
        elif mem[i] == 99:
            i+=1 #just in case so we don't infinite loop
            break
        else:
            #print(intcode[i])
            raise Exception("unknown opcode")
    return mem

assert run_intcode([1,0,0,0,99]) == [2,0,0,0,99]
assert run_intcode([2,3,0,3,99]) == [2,3,0,6,99]
assert run_intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert run_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

with open(r'C:\Users\david\Documents\advent_of_code\input2_1.txt','r') as infile:
    reader = csv.reader(infile,delimiter=',')
    for row in reader:
        intcode=[int(r) for r in row]

modified_code=copy.copy(intcode)
modified_code[1]=12
modified_code[2]=2
processed_code = run_intcode(modified_code)
print(processed_code[0])

#Day 2, Part 2

target_output=19690720

for x in range(0,100):
    for y in range(0,100):
        modified_code=intcode
        modified_code[1]=x
        modified_code[2]=y
        try:
            processed_code = run_intcode(modified_code)
        except:
            processed_code=[0]
        if processed_code[0] == target_output:
            break
    if processed_code[0] == target_output:
            break

print(100*x + y)


# In[ ]:




