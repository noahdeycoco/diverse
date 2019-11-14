# /usr/bin/env python3
# coding: utf-8

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(bag):
    print('Inventory:')
    total_items = 0
    for items, number in bag.items():
        print(number, items)
        total_items += number
    print('Total number of items: ' + str(total_items))


def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    print(str(len(addedItems)) + ' has been added.')
    return inventory


if __name__ == '__main__':
    # displayInventory(stuff)
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
