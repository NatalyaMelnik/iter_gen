result_list = [['a', ['b'], 'c'],
               ['d', 'e', ['f'], 'h', False],
               [1, 2, None], ]
st = []
st.append(result_list)


class FlatIterator:
    def __init__(self, st):
        self.st = []

        while len(st):
            l = st.pop()
            for x in l:
                if type(x) is list:
                    st.append(x)
                else:
                    print(x)

    def __iter__(self):
        return iter(self.st)




t = FlatIterator(result_list)
it = iter(t)
for item in t:
    print(item)

