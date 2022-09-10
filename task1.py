class FlatIterator:
    def __init__(self, lst):
        self.rows = len(lst)
        self.lst = list()
        for i in range(self.rows):
            self.lst.extend(lst[i][0: i + len(nested_list)])

    def __iter__(self):
        return iter(self.lst)


nested_list = [['a', 'b', 'c'],
                     ['d', 'e', 'f', 'h', False],
                     [1, 2, None], ]

ls_one = [x for row in nested_list for x in row]

t = FlatIterator(nested_list)
it = iter(t)
for item in t:
    print(item)

l = []
for i in range(len(nested_list)):
    l.extend(nested_list[i][0: i + len(nested_list)])
print(l)


