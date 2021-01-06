import json
import random


AFFIXES = json.loads(open('data/affixes.json', 'r').read())
BASE_STATS = json.loads(open('data/base_stats.json', 'r').read())
TIERS_CONFIG = json.loads(open('data/tiers_config.json', 'r').read())


def get_affix_by_id(id, group='uncommon'):

	for a in AFFIXES[group]:
		if a['id'] == id:
			return a
	return {}


def get_random_affix(group='uncommon'):

	return random.choice(AFFIXES[group])


def get_non_overlapping_affix(selected=[], group='uncommon'):

	affix = get_random_affix(group)

	while any(a['id'] == affix['id'] for a in selected):
		affix = get_random_affix(group)

	return affix


def parse_affix(affix):

	parsed_affix = {}
	parsed_affix['id'] = affix['id']
	parsed_affix['text'] = affix['text']
	parsed_affix['values'] = []

	for var in affix['vars']:
		key = var['key']
		type_ = var['type']
		values = var['values']

		if type_ == 'rand':
			value = random.randint(values[0], values[1])
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
