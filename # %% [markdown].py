# %% [markdown]
# Создание Git репозитория:
# * git remote --verbose
# * git config --get commit.template
# * git push -u origin master

# %% [markdown]
# * [new branch]      master -> master

# %% [markdown]
# Типы данных в Python:
# * строки(string)

# %%
string1 = 'string'
print(string1*2, string1[-3:], string1[::-1])

# %% [markdown]
# * Список (List)

# %%
list1 = [10, 20, 30, "word1", "word2"]
list2 = list(string1)
print(list1, list1[::-1], list1[2:4])
print(list2, sorted(list2))

# %% [markdown]
# * Dictionaries (словари)

# %%
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(london['name'], london['location'], london['vendor'])

# %% [markdown]
# * Tuples (кортежи)

# %%
tuple = ('hostname', 'location', 'vendor', 'model', 'ios', 'ip')
print(sorted(tuple))


tuple[1] = 'test' # Нельзя изменять элементы кортежа


# %% [markdown]
# * Sets (множества)

# %%
set1 = {100, 101, 102, 200}
set2 = {10, 20, 30, 50, 100}
print(set1 & set2) # Пересечение
print(set1 | set2) # Объединение
print(set1 - set2) # Разность
print(set1 ^ set2) # Симметрическая разность

# %% [markdown]
# * Boolean (логический тип данных)

# %%
bool1 = True
bool2 = False
if (bool1): print("hello")
if (bool2): print("world")


