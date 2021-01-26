import json
import random


AFFIXES = json.loads(open('data/affixes.json', 'r').read())
TYPES = json.loads(open('data/types.json', 'r').read())
TIERS = json.loads(open('data/tiers.json', 'r').read())
CONFIG = json.loads(open('data/config.json', 'r').read())

SOCKET_ID = 999
SCALE_MAP = {'Common': 0, 'Magic': 1, 'Rare': 2, 'Legendary': 3, 'Unique': 4}

def _get_scale(affix, tier):

	scale = 0.0 if tier is None else TIERS[tier]['v_scale']

	if 'v_scale' in affix:
		scale = affix['v_scale'][SCALE_MAP[tier]]

	return scale


def get_affix_by_id(id):

	str_id = str(id)
	for g in AFFIXES:
		if str_id in AFFIXES[g]:
			return AFFIXES[g][str_id]
	return None


def get_random_affix(groups=['Common']):

	pool = []
	for g in groups:
		if g in AFFIXES:
			pool = list(set(pool) | set(AFFIXES[g]))

	if pool == []:
		return None

	return get_affix_by_id(id=random.choice(pool))


def get_non_overlapping_affix(selected=[], groups=['Common']):

	affix = get_random_affix(groups)

	while any(affix['id'] == a['id'] for a in selected):
		affix = get_random_affix(groups)

	return affix


def parse_affix(affix, tier=None):

	scale = _get_scale(affix, tier)

	parsed_affix = {}
	parsed_affix['id'] = affix['id']
	parsed_affix['text'] = affix['text']
	parsed_affix['values'] = []

	for var in affix['vars']:
		key = var['key']
		type_ = var['type']
		values = var['values']

		if type_ in ['rand', 'frand']:
			min_ = values[0] + values[0] * scale
			max_ = values[1] + values[1] * scale

			if type_ == 'rand':
				value = random.randint(int(min_), int(max_))
			else:
				value = round(min_ + random.random() * (max_-min_), 2)

		elif type_ == 'choice':
			value = random.choice(values)
		elif type_ == 'value':
			value = values[0]

		parsed_affix['values'].append([key, value])

	return parsed_affix


def format_affix(parsed_affix):

	text = parsed_affix['text']

	for key, value in parsed_affix['values']:
		text = text.replace(key, str(value))

	return text
