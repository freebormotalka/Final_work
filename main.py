#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
#Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
unique_values = data['whoAmI'].unique() #Получаем уникальные значения тз столбца "WhoAmI"
one_hot_data = pd.DataFrame() #Создаем пустой датафрэйм
#Для каждого уникального значения создаем новый столбец и заполняем его значениями от 0 до 1
for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)
one_hot_data.head()