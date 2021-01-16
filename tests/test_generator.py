import random

from src.items import *
from src.data import *


def test_create_item_1():

	# no arguments
	assert create_random_item() != {}, 'Should have created a non empty dict'

def test_create_item_2():

	# passing tier
	tiers = list(TIERS.keys())
	for t in tiers:
		item = create_random_item(tier=t)
		assert item['tier'] == t, f'TIER is {item["tier"]}, should be {t}'

def test_create_item_3():

	# passing type
	types = list(TYPES)
	for t in types:
		item = create_random_item(type_=t)
		assert item['type'] in TYPES, f'TYPE is {item["type"]}, should be {t}'

def test_create_item_com_affixes_1():

	affixes = [1000, 1001, 1002, 1003, 999]
	item = create_item_with_affixes(affixes, tier='Rare')
	assert has_affixes(item, affixes), 'Item should have those affixes'

def test_has_affixes_1():

	item = create_random_item()
	affix = get_affix_by_id(999)
	item['sockets'].append(affix)
	assert has_affixes(item, [999]) == True, 'The item should have the affix'

def test_has_affixes_2():

	item = create_random_item()
	item['sockets'].clear()
	assert has_affixes(item, [999]) == False, 'The item should NOT have the affix'


def run_tests():

	test_create_item_1()
	test_create_item_2()
	test_create_item_3()

	test_create_item_com_affixes_1()

	test_has_affixes_1()
	test_has_affixes_2()

	print('[generator] All tests completed')


if __name__ == '__main__':
	run_tests()