from src.data import *


def create_random_item(tier=None, type_=None):

	if tier is None:
		tier = random.choice(list(TIERS))

	if type_ is None:
		type_ = random.choice(list(TYPES))

	# ---

	scale = TIERS[tier]['v_scale']
	stats = []
	affixes = []
	sockets = []

	for id in TYPES[type_]['affixes']:
		stats.append(parse_affix(get_affix_by_id(id), scale))

	for r in TIERS[tier]['s_rates']:
		if random.random() < r:
			sockets.append(parse_affix(get_affix_by_id(SOCKET_ID), scale))

	diff = len(TIERS[tier]['rates']) - len(sockets)
	for r in TIERS[tier]['rates'][:diff]:
		if random.random() < r:
			affix = get_non_overlapping_affix(affixes, ['Common', type_])
			affixes.append(parse_affix(affix, scale))

	if tier == "Legendary":
		affix = get_random_affix(['Legendary', 'l_'+type_,]) #temp
		affixes.append(parse_affix(affix))

	item = {}
	item['name'] = "ITEM NAME"
	item['tier'] = tier
	item['type'] = type_
	item['stats'] = stats
	item['affixes'] = affixes
	item['sockets'] = sockets

	return item


def create_item_with_affixes(ids=[], tier=None, type_=None):

	item = create_random_item(tier=tier, type_=type_)
	tier = item['tier']
	type_ = item['type']
	scale = TIERS[tier]['v_scale']

	affixes = []
	sockets = []
	for id in ids:
		affix = parse_affix(get_affix_by_id(id), scale)
		if id == SOCKET_ID:
			sockets.append(affix)
		else:
			affixes.append(affix)

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


def has_affixes(item, ids=[]):

	affixes = []
	affixes.extend(item['stats'])
	affixes.extend(item['affixes'])
	affixes.extend(item['sockets'])

	list_ids = [a['id'] for a in affixes]

	for id in ids:
		if id not in list_ids:
			return False 
	return True


def to_view(item):

	view_dict = {}
	view_dict['name'] = item['name']
	view_dict['tier'] = item['tier']
	view_dict['type'] = item['type']
	view_dict['stats'] = []
	view_dict['affixes'] = []
	view_dict['sockets'] = []

	for stat in item['stats']:
		view_dict['stats'].append(format_affix(stat))
	for affix in item['affixes']:
		view_dict['affixes'].append(format_affix(affix))
	for socket in item['sockets']:
		view_dict['sockets'].append(format_affix(socket))

	return view_dict
