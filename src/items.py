from src.data import *


def create_random_item(tier=None, type_=None):

	if tier is None:
		tier = random.choice(list(TIERS))

	if type_ is None:
		type_ = random.choice(list(TYPES))

	# ---

	stats = []
	affixes = []
	legendary = []
	sockets = []

	for id in TYPES[type_]['affixes']:
		stats.append(parse_affix(get_affix_by_id(id), tier))

	for r in TIERS[tier]['s_rates']:
		if random.random() < r:
			sockets.append(parse_affix(get_affix_by_id(SOCKET_ID), tier))

	diff = len(TIERS[tier]['rates']) - len(sockets)
	for r in TIERS[tier]['rates'][:diff]:
		if random.random() < r:
			affix = get_non_overlapping_affix(affixes, ['Common', type_])
			affixes.append(parse_affix(affix, tier))

	if tier == "Legendary":
		affix = get_random_affix(['Legendary', 'l_'+type_,]) #temp
		legendary.append(parse_affix(affix))

	item = {}
	item['name'] = "ITEM NAME"
	item['tier'] = tier
	item['type'] = type_
	item['stats'] = stats
	item['affixes'] = affixes
	item['legendary'] = legendary
	item['sockets'] = sockets

	return item


def create_item_with_affixes(ids=[], tier=None, type_=None):

	item = create_random_item(tier=tier, type_=type_)
	tier = item['tier']
	type_ = item['type']

	affixes = []
	sockets = []
	for id in ids:
		affix = parse_affix(get_affix_by_id(id), tier)
		if id == SOCKET_ID:
			sockets.append(affix)
		else:
			affixes.append(affix)

	item['affixes'] = affixes
	item['sockets'] = sockets

	return item


def create_unique_item(affix_ids, tier, type_, name):

	pass


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

	names = [
		'Boots of Perilous Thread',
		'Tunic of Perilous Thread',
		'Boots of Chilling Frost',
		'Ring of Three Curses',
		'Vengeful Oak Wand of Overpower',
		'Ghoul Strike',
		'Immobilizing Mythical Staff',
		'Staff of Ursine Strength'
	]

	view_dict = {}
	view_dict['name'] = random.choice(names) #TODO
	view_dict['tier'] = item['tier']
	view_dict['type'] = item['type']
	view_dict['stats'] = []
	view_dict['affixes'] = []
	view_dict['legendary'] = []
	view_dict['sockets'] = []

	for stat in item['stats']:
		view_dict['stats'].append(format_affix(stat))
	for affix in item['affixes']:
		view_dict['affixes'].append(format_affix(affix))
	for affix in item['legendary']:
		view_dict['legendary'].append(format_affix(affix))
	for socket in item['sockets']:
		view_dict['sockets'].append(format_affix(socket))

	view_dict['main_stat'] = view_dict['stats'].pop(0) #temp
	view_dict['sell_value'] = 999
	view_dict['durability'] = 100

	dmg_icon = 'default'
	if item['type'] in CONFIG['offensive']:
		dmg_icon = 'offensive'
	elif item['type'] in CONFIG['defensive']:
		dmg_icon = 'defensive'
	view_dict['dmg_icon'] = dmg_icon

	return view_dict
