#Helps list all of the 2nd tier outcomes in outcomes.json file
import json
outcomes = json.loads(open("outcomes.json").read())

low_levels = []
for (k, v) in outcomes.items():
  for (k2, v2) in v["Children"].items():
    for k3 in v2["Children"].keys():
      low_levels.append(k3)

print(len(low_levels))

for outcome in low_levels: print(outcome)