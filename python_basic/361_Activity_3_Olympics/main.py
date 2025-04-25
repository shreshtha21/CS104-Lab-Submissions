'''
    Olympics Medals
    Author: Saksham Rathi
'''

from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required = True)
args = parser.parse_args()

# dictionary for the data
totalData = {}

# looping through the directory
for fileName in os.listdir(args.path):

    # read the file
    with open(os.path.join(args.path,fileName), "r") as file:
        for line in file:
    # loop through data of file and set the values for the data
            country,gold,silver,bronze=line.strip().split("-")
            gold,silver,bronze= int(gold),int(silver),int(bronze)
            if country in totalData:
                totalData[country][0]+=gold
                totalData[country][1]+=silver
                totalData[country][2]+=bronze
            else:
                totalData[country] = [gold,silver,bronze]



# sort as per gold medals and break ties lexicographically
sortedData = dict(sorted(totalData.items(), key=lambda x: (-x[1][0], x[0])))
print(sortedData)
