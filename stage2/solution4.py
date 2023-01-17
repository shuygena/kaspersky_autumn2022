import pandas as pd
import matplotlib.pyplot as plt

def get_formated_date(d):
    return int(d.split()[0].split('-')[2])

def get_formated_time(d):
    return d.split()[1][:5]

def plot_url(d):
    df = d.copy()
    df['time'] = df['created'].apply(get_formated_time)
    df = df.drop(columns=['created', 'source'])
    df.rename(columns={'id': 'count url'}, inplace=True)
    df = df.pivot_table(index = ['time'], aggfunc ='count') # получила таблицу
    df.plot() # вывод графика
    plt.title('count per minute')
    plt.show()

def pivot_table(d):
    df = d.copy()
    df['day'] = df['created'].apply(get_formated_date) # создаю столбец day с днями 1, 2, 3...
    df = df.drop(columns=['created', 'source']) # удаляю 2 столбца
    df.rename(columns={'id': 'count'}, inplace=True) # переименовываю столбец id в count
    df = df.pivot_table(index = ['day'], aggfunc ='count') # получаю сводную таблицу, где day - индекс
    df = df.reset_index(level=0) # перевожу индексы в отдельный столбец
    print(df.to_string(index=False)) # вывод столбцов day и count без индексов

def get_source_percentage(d):
    df = d.copy()
    df = df.drop(columns=['created'])
    df.rename(columns={'id': 'percent'}, inplace=True)
    func = lambda x: 100*x.count()/df.shape[0]
    df = df.pivot_table(index = ['source'], aggfunc = func)
    print(df)
    low_percent = df[df['percent'] < 1]
    print("\nКоличество  источников, из которых пришло менее 1% урлов:", low_percent.shape[0])
    print()
    
def task4():
    df = pd.read_csv('urls_with_source.csv', delimiter=',')
    get_source_percentage(df) # первое задание 
    pivot_table(df) # второе задание
    plot_url(df) # третье задание

if __name__ == "__main__":
    task4()