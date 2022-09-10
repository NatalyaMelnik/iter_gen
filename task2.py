class Flat_generator():
    def __init__(self, lst):
        self._lst = lst

    def __iter__(self):
        for i in range(len(self._lst)):
            for j in range(len(self._lst)):
                yield self._lst[i][j] # генератор используем


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

ls_one = [x for row in nested_list for x in row]

t = Flat_generator(nested_list)
it = iter(t)
for item in t:
    print(item)


print(ls_one)
print(type(it)) # генератор, можно спокойно применить метод next b=next(it)


