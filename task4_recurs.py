base_list = [1, [2, 3], 4, [[6, 7]]]


def get_element(base_list, result_list=None):
    if result_list is None:
        result_list = []
    for element in base_list:
        if type(element) == list:
            get_element(element, result_list)
            yield from get_element(element)

        else:
            result_list.append(element)

            yield element


for i in get_element(base_list):
    print(i)

