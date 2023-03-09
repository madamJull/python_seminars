import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst) # возвращает перемешанную последовательность
# data = pd.DataFrame({'whoAmI lst'})
# data.head()
print(lst)