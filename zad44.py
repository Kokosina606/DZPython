#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
#Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

#import random
#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI':lst})
#data.head()

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print (lst)
data = pd.DataFrame({'whoAmI':lst})
lst_robot=[1 if x=='robot' else 0 for x in lst]
lst_human=[1 if x=='human' else 0 for x in lst]
data=pd.DataFrame(data={'human':lst_human, 'robot':lst_robot})
data.head()
print (data)