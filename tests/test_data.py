#import random

from src.data import *


def test_get_affix_by_id_1():

	# valid ids
	ids = [0, 999, 1000, 2000, 3000]
	for id in ids:
		affix = get_affix_by_id(id)
		assert affix is not None, f'Affix id {id} should not be NONE'


def test_get_affix_by_id_2():

	# invalid id
	affix = get_affix_by_id(-1)
	assert affix == None, 'Return for invalid id should be None'


def test_get_random_affix_1():

	# no arguments
	affix = get_random_affix()
	assert type(affix) is dict, 'Returned value is not a dict'

def test_get_random_affix_2():

	# valid groups
	affix = get_random_affix(['Basic', 'Common', 'Legendary'])
	assert type(affix) is dict, 'Returned value for valid groups is not a dict'

def test_get_random_affix_3():

	# invalid groups
	affix = get_random_affix(['undefined'])
	assert affix is None, 'Returned for invalid group should be None'

def test_get_random_affix_4():

	# mix of valid and invalid
	affix = get_random_affix(['Basic', 'undefined', 'Legendary'])
	assert type(affix) is dict, 'Returned value for valid groups is not a dict'

def test_get_non_overlapping_affix_1():

	affix = get_non_overlapping_affix()
	assert type(affix) == dict, 'Type of return should be dict'

def test_get_non_overlapping_affix_2():

	affix = get_non_overlapping_affix(groups=['Common', 'Legendary'])
	assert type(affix) == dict, 'Type of return should be dict'

def test_parse_item_1():

	random.seed(a=0)
	mock_affix = {'id': 1038, 'text': '+<A> Maximum Mana (Sorcerer Only)', 'values': [['<A>', 59]]}
	affix = parse_affix(get_affix_by_id(1038))
	assert affix == mock_affix, 'The parsed affix should be the same'

def test_format_affix_1():

	affix = get_random_affix()
	parsed_affix = parse_affix(affix)
	formatted_affix = format_affix(parsed_affix)
	
	text = parsed_affix['text']
	for key, value in parsed_affix['values']:
		text = text.replace(key, str(value))
	assert formatted_affix == text, 'The formatted affix is incorrect'

def run_tests():

	test_get_affix_by_id_1()
	test_get_affix_by_id_2()

	test_get_random_affix_1()
	test_get_random_affix_2()
	test_get_random_affix_3()
	test_get_random_affix_4()

	test_get_non_overlapping_affix_1()
	test_get_non_overlapping_affix_2()

	test_parse_item_1()

	test_format_affix_1()

	print('[data] All tests completed')

if __name__ == '__main__':
	
	run_tests()
