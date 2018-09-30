import csv
import os
import operator
from collections import defaultdict

f = open("Polling Output.txt", "w")
csv_path = "Resources/election_data.csv"

with open(csv_path) as poll_data:
    reader = csv.reader(poll_data)
    next(reader)
    candidate = []
    voter_id = []
    county= []
    Li = 0
    Khan = 0
    Correy = 0
    Tooley = 0
    for row in reader:
        candidate.append(row[2])
        if row[2] == "O'Tooley":
          Tooley = Tooley +1
        if row[2] == "Khan":
          Khan = Khan +1
        if row[2] == "Li":
          Li = Li +1
        if row[2] == "Correy":
          Correy = Correy +1
    can_set = list(set(candidate))
    all_names = Correy + Li + Tooley + Khan
    per_Li = Li/all_names*100
    per_Khan = Khan/all_names*100
    per_Correy = Correy/all_names*100
    per_Tooley = Tooley/all_names*100

    print("Election Results")
    f.write("Financial Analysis")
    f.write('\n')
    print("-------------------------")
    f.write("-------------------------")
    f.write('\n')
    print(f"Total Votes: {all_names}")
    f.write(f"Total Votes: {all_names}")
    f.write('\n')
    print("-------------------------")
    f.write("-------------------------")
    f.write('\n')
    print(f"Li: {per_Li}% ({Li})")
    f.write(f"Li: {per_Li}% ({Li})")
    f.write('\n')
    print(f"Khan: {per_Khan}% ({Khan})")
    f.write(f"Khan: {per_Khan}% ({Khan})")
    f.write('\n')
    print(f"Correy: {per_Correy}% ({Correy})")
    f.write(f"Khan: {per_Khan}% ({Khan})")
    f.write('\n')
    print(f"O'Tooley: {per_Tooley}% ({Tooley})")
    f.write(f"Khan: {per_Khan}% ({Khan})")
    f.write('\n')
    print("-------------------------")
    f.write("-------------------------")
    f.write('\n')
    print(f"Winner: Khan!")
    f.write(f"Winner: Khan!")
    f.write('\n')
    
f.close()




