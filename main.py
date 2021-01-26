from tests import test_data, test_generator

test_data.run_tests()
test_generator.run_tests()

from flask_app import app
app.app.run()

from src.items import *

# print(create_random_item(tier='Common'))
# print(create_random_item(tier='Magic'))
# print(create_random_item(tier='Rare'))
# print(create_random_item(tier='Legendary'))

# print_item(create_random_item(tier='Legendary', type_='Sword'))

print_item(create_item_with_affixes([3000], type_='Boots', tier='Common'))
print_item(create_item_with_affixes([3000], type_='Boots', tier='Magic'))
print_item(create_item_with_affixes([3000], type_='Boots', tier='Rare'))
print_item(create_item_with_affixes([3000], type_='Boots', tier='Legendary'))

# create_random_item(tier='Legendary')
# create_random_item(tier='Legendary')
# create_random_item(tier='Legendary')

# print_item(create_item_with_affixes([3000], type_='Boots'))
# print_item(create_item_with_affixes([4000], type_='Boots', tier='Legendary'))

# print_item(create_random_item())
# print_item(create_random_item())
# print_item(create_random_item(tier='Common'))
# print_item(create_random_item(type_='Helm'))
# print_item(create_random_item(type_='Sword'))
# print_item(create_random_item(tier='Rare', type_='Sword'))
# print_item(create_random_item(tier='Legendary', type_='Boots'))
# print_item(create_random_item(type_='Two-Handed Sword'))

