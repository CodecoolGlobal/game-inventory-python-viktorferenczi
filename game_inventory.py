inv = {"rope":1,"torch":6,"gold coin":42,"dagger":1,"arrow":12}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

def display_inventory(inventory):                       #display the inventory normally

    for i in inventory:
        print(i + ":" + " " +str(inventory[i]))



def add_to_inventory(inventory, added_items):           #add item to the inventory

    for loot in dragon_loot:
        if loot in inventory.keys():
            inventory[loot] +=1
        else:
            inventory.update({loot:1})



def print_table(inventory,order = None):                #display the inventory with style

    max = 0
    for x in inventory:
        for y in inventory:
            if len(x) >= len(y):
                if max <len(x):
                    max = len(x)
    line = "-" * (max+8)
    space = " "
    print(line + "\n" + space *(max-9) + "item name" + " | count\n" + line)

    if order == "count,desc":
        sortedtuple_desc = sorted(inventory.items(), key=lambda x: x[1], reverse = True)
        sorteddict_desc = dict(sortedtuple_desc)
        for loot in sorteddict_desc:
            space = " "
            print(space * (max - len(loot)) + loot + " |" + space * (5 - len(str(inventory[loot]))) + str(inventory[loot]))
    elif order == "count,asc":
        sortedtuple_asc = sorted(inventory.items(), key=lambda x: x[1])
        sorteddict_asc = dict(sortedtuple_asc)
        for loot in sorteddict_asc:
            space = " "
            print(space * (max - len(loot)) + loot + " |" + space * (5 - len(str(inventory[loot]))) + str(inventory[loot]))
    elif order is None:
        for loot in inventory:
            space = " "
            print(space *(max - len(loot)) + loot + " |" + space *(5-len(str(inventory[loot]))) + str(inventory[loot]))
    else:
        exit()

    print(line)


def import_inventory(inventory,filename = "test_inventory.csv"):          #import inventory from a file

    file = open(filename,"r")
    x = file.read()
    separated = x.split(",")
    for loot in separated:
        if loot in inventory.keys():
            inventory[loot] += 1
        else:
            inventory.update({loot: 1})
    file.close()



def export_inventory(inventory,filename = None):                            #export inventory into a file

    if filename is None:
        file = open("export_inventory.csv", "w")
        for item in inventory:
            file.write(item+",")
        file.close()
    else:
        file_chosen = open(filename, "w")
        for item in inventory:
            file_chosen.write(item+",")
        file_chosen.close()
