from src.items import *

#examples
print_item(create_item(tier='Common'))
print_item(create_item(tier='Magic'))
print_item(create_item(tier='Rare'))
print_item(create_item(tier='Legendary'))

#generating gear of specific type
print_item(create_item(tier='Legendary', type_='Sword'))
print_item(create_item(tier='Legendary', type_='Sword'))
