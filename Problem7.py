# Problem: https://adventofcode.com/2020/day/7
# Solution - Create a dictionary mapping of parent bag with a set of child bags
# bag1 : (bag2, bag3, bag4)
# bag2 : (bag7, bag8)
# when searching for a bag,


def create_parent_set(list_lines):
    # Takes a list of lines as input and returns a dictionary
    # split the line into list of child bags
    # for each child, add the parent in dictionary set
    #
    # A -> B, C, D
    # B -> F, G, H
    # D -> H
    # H -> Z
    #
    # B: (A)
    # C: (A)
    # D: (A)
    # F: (B)
    # G: (B)
    # H: (B,D)
    # Z: (H)
    import re
    dict_bags = {}
    patt_1 = re.compile('  contain')
    patt_2 = re.compile(' [0-9] ')
    patt_3 = 'bags'
    patt_4 = 'bag'
    patt_5 = r'\.'
    for line in list_lines:
        line = re.sub(patt_2, '', line)
        line = re.sub(patt_3, '', line)
        line = re.sub(patt_4, '', line)
        line = re.sub(patt_5, '', line)
        parent, child = patt_1.split(line)
        list_child = [x.strip() for x in child.split(',')]

        for child in list_child:
            # Create the dictionary the first time
            if child not in dict_bags:
                dict_bags[child] = set()

            dict_bags[child].add(parent)
            # pass
    return dict_bags


def find_all_parents(dict_parents, bag_to_find):
    # Takes the dictionary as input and bag to find. get the parents of bag to find and add them to global set.
    # Then iterate over the parents in a recursive manner and find their parents and then their parent and so on
    # Finally return the
    if bag_to_find in dict_parents:
        set_parents.update(dict_parents[bag_to_find])
        set_parent = dict_parents[bag_to_find]
        for parent in set_parent:
            find_all_parents(dict_parents, parent)
    else:
        return
    print(f"parents of {bag_to_find} are {set_parent}")
    # Nothing to return because the set_parents is coming from main call


if __name__ == '__main__':
    bag_to_search = 'shiny gold'
    with open('Data/Problem7.txt') as file:
        list_input_7 = file.readlines()
        list_input_7 = [x.strip() for x in list_input_7]
    # dict_bag = {}
    set_parents = set()
    dict_bag = create_parent_set(list_input_7)
    # print(dict_bag)
    find_all_parents(dict_bag, bag_to_search)
    print(f"Final Parents of {bag_to_search} are {set_parents}")
    print(len(set_parents))
