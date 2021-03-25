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

    if bag_to_find in dict_parents:
        set_parents.update(dict_parents[bag_to_find])
        set_parent = dict_parents[bag_to_find]
        for parent in set_parent:
            find_all_parents(dict_parents, parent)
    else:
        return
    # print(f"parents of {bag_to_find} are {set_parent}")
    # Nothing to return because the set_parents is coming from main call


def create_bag_tuples(list_lines):
    # Returns a dictionary, each key as a bag and value as a set of Tuples
    # containing number of bags and color
    # e.g.,
    # light orange bags contain 1 shiny gold bag, 3 dim maroon bags, 5 striped green bags, 2 pale aqua bags.
    # wavy bronze bags contain 3 shiny gold bag, 5 bright turquoise bags, 4 pale orange bags.
    # Above 2 lines will return
    # {
    # light orange: {(1, shiny gold), (3, dim maroon), (5, striped green), (2, pale aqua)},
    # wavy bronze: {(3, shiny gold), (5, bright turquoise), (4, pale orange)}
    # }
    import re
    dict_tuples = {}
    patt_1 = re.compile('  contain')
    patt_3 = 'bags'
    patt_4 = 'bag'
    patt_5 = r'\.'
    for line in list_lines:
        line = re.sub(patt_3, '', line)
        line = re.sub(patt_4, '', line)
        line = re.sub(patt_5, '', line)
        parent, child = patt_1.split(line)
        list_child = [x.strip() for x in child.split(',')]

        # Check for empty bags
        if list_child[0] != 'no other':

            # Creating a set of tuples, each tuple derived from splitting the string at
            # first occurrence of space
            # I LOVE PYTHON!!
            dict_tuples[parent] = set(tuple(x.split(' ', 1)) for x in list_child)
    return dict_tuples


def count_bags_inside(dict_tuples, bag):
    if bag in dict_tuples:
        count = 0
        for tup in dict_tup[bag]:
            count += int(tup[0]) + (int(tup[0]) * int(count_bags_inside(dict_tuples, tup[1])))
        # print(f"{bag} contains {count} bags")
        return int(count)
    else:
        return 0


if __name__ == '__main__':
    bag_to_search = 'shiny gold'
    with open('Data/Problem7.txt') as file:
        list_input_7 = file.readlines()
        list_input_7 = [x.strip() for x in list_input_7]
    set_parents = set()
    dict_bag = create_parent_set(list_input_7)
    find_all_parents(dict_bag, bag_to_search)
    print(f"Final Parents of {bag_to_search} are {set_parents}")
    print(len(set_parents))
    dict_tup = create_bag_tuples(list_input_7)
    # print(dict_tup)
    final_count = count_bags_inside(dict_tup, bag_to_search)
    print(f"{bag_to_search} contains {final_count} bags")
