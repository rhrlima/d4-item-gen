from src.data import *


def create_item(tier, type_=None):

	if type_ is None:
		type_ = random.choice(list(BASE_STATS.keys()))

	base_stats = []
	for entry in BASE_STATS[type_]:
		stat = parse_affix(get_affix_by_id(entry['id'], entry['group']))
		base_stats.append(stat)

	affixes = []
	sockets = []
	for r in TIERS_CONFIG[tier]['rates']:
		if random.uniform(0, 1) < r:
			if random.uniform(0, 1) < 0.3:
				affix = get_affix_by_id(999, 'common')
				sockets.append(parse_affix(affix))
			else:	
				affix = get_non_overlapping_affix(affixes, 'uncommon')
				affixes.append(parse_affix(affix))

	if tier == "Legendary":
		affix = get_non_overlapping_affix(affixes, 'legendary')
		affixes.append(parse_affix(affix))

	
	

	item = {}
	item['name'] = "ITEM NAME"
	item['tier'] = tier
	item['type'] = type_
	item['stats'] = base_stats
	item['affixes'] = affixes
	item['sockets'] = sockets

	return item
	

def print_item(item):

	print(item['name'])
	print(item['tier'], item['type'])

	print('---')
	for a in item['stats']:
		print(format_affix(a))

	print('---')
	for a in item['affixes']:
		print(format_affix(a))

	for s in item['sockets']:
		print(format_affix(s))
