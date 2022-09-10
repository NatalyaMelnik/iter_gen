a = [[[1, 2], [3, 4]], [5]]
def generator(st):
    st = []
    st.append(a)
    while len(st):
        l = st.pop()
        for x in l:
            if type(x) is list:
                st.append(x)
            else:
                yield x


it = generator(a)
print(it)  # объект генератор
for i in it:
    print(i)
# print(next(it))
# print(next(it))

