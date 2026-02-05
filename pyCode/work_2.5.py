print(list(map(lambda x: x**2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

name =['张三','李四']
print(list(map(lambda x:'QG_' + x, name)))

raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99","120"]
numbers = []
big_number = []
right_number= []
def find_number(s):
     for i in s:
         try:
             numbers.append(int(i))
         except ValueError:
                    pass
find_number(raw_data)

for j in numbers:
    if j >= 80:
        right_number.append(j)
max = max(right_number)
min = min(right_number)
for k in big_number:
    right_number.append(k)
for l in right_number:
    a = (l - min) / (max - min)
    a += 0.5
    print(a)
    print(l)
    if a > 1.0:
        print("核心过载")
    else:
        print("核心正常")