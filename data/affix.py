import json

AFFIXES = json.loads(open('affixes.json', 'r').read())

new_affixes = {}

for g in AFFIXES:
	print(g)

	if g not in new_affixes:
		new_affixes[g] = {}

	for a in AFFIXES[g]:

		new_affixes[g][a['id']] = a

#print(new_affixes)

#json.dump(new_affixes, open('affixes2.json', 'w'))

AFFIXES2 = json.load(open('affixes2.json', 'r'))

print(AFFIXES2['common']['0'])
print(AFFIXES2['common'][0])