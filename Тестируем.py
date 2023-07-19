numbers_Fibo=[1] #создаем список, в который будем закидывать числа Фибоначчи
n1,n2,n=1,1,0 #n1=1 изначально первый член, n2- второй и n- это сумма двух предыдущих членов(новый член)
while n<10**10: #именно такое условие,в списке окажется одно число большее 10**10
    n=n1+n2 # создали новый член
    numbers_Fibo.append(n)#добавили в список
    n1,n2=n2,n #меняем значения предыдущих членов, чтобы последовательность двигалась

digits='0123456789' # при прохождении через символы строки будем проверять цифра ли это
res=0 #итоговая результирующая
with open('24-1.txt')as f:
    for s in f:
        stroka_number='' #создаем пустую строку, чтобы потом формировать число, приклеивая символ-цифру к данной строке
        b,flag,m=[],True,0 # b-список, который будет хранить индексы первых цифр всех найденных чисел Фибоначчи
        # флаг-чтобы сохранять индекс первой цифры числа и опускать его, чтобы индексы других цифр не сохранялись
        #переменная m будет хранить максимальное число Фибоначчи в строке
        for x in range(len(s)):
            if s[x] in digits: #если символ - это цифра
                stroka_number+=s[x] #прибавляем его к строке, даже если это 0. int()уберет его впоследствии
                if flag and s[x]!='0': #зайдёт, если это первая цифра числа ( не 0) и сохранит её индекс
                    thirst_index=x
                    flag=False
            else:# если символ - это не цифра (буква)
                if len(stroka_number)!=0:
                    if int(stroka_number)in numbers_Fibo:#если строка не пустая, то через int()проверяем-это число Фибоначчи?
                        b.append(thirst_index)#добавляем в список индекс первой цифры числа Фибоначчи
                        m=max(m,int(stroka_number))#максимальное число Фибоначчи(понадобится, если строка хорошая)
                stroka_number='' #ищем другое число
                flag=True
        for t in range(0,len(b)-1): #в списке b - индексы первых цифр чисел Фибоначчи
            if 'F'and'L'and'A'and'S'and 'H'in s[b[t]:b[t+1]+1]: # срезами мы делаем промежуток от одного до другого числа
                res=max(res,m)#максимальное из всех найденных чисел Фибоначчи(если хороших строк несколько)
print(res)

numbers_Fibo=[1] #создаем список, в который будем закидывать числа Фибоначчи
n1,n2,n=1,1,0 #n1=1 изначально первый член, n2- второй и n- это сумма двух предыдущих членов(новый член)
while n<10**10: #именно такое условие,в списке окажется одно число большее 10**10
    n=n1+n2 # создали новый член
    numbers_Fibo.append(n)#добавили в список
    n1,n2=n2,n #меняем значения предыдущих членов, чтобы последовательность двигалась

'''res=0 # итоговая результирующая, где будет максимальное число Фибоначчи
digits='0123456789' #создаем искусственно цифры, чтобы потом при проверке элемента, понять что перед нами число
with open('24-1.txt')as f: # открываем файл
    for s in f:
        for x in s: # проходимся по элементам всей строки
            if x not in digits: #если это не цифра, то далее надо проверить нужные буквы
                if x in 'FLASH':
                    s=s.replace(x,'*'+str(x)+'*') #мы заменяем нужные буквы, чтобы потом при сплите они не склеились с числами
                else:s=s.replace(x,'*')  #всё остальное(кроме чисел и нужных букв) заменяем
        s=' '.join(s.split('*')).split() #сначала идёт сплит по звёздам- получается список, в котором есть ненужные пустоты
        #мы с помощью join склеиваем всё в строку и делаем сплит по пробелам, получается хороший список
        flag,n=True,'*'     #создаем флаг, чтобы потом, если строка хорошая, мы опустили его и не проверяли ненужное
        # переменная n будет хранить индекс числа Фибоначчи, изначально *, потому что не известно найдётся ли число
        for i in range(0,len(s)):
            if s[i] not in 'FLASH': #если нашлось число
                if int(s[i])in numbers_Fibo: #проверка на то, что число является именно числом Фибоначчи
                    if flag:       #заходит, если не доказано, что строка хорошая
                        if n=='*': #если число Фибоначчи встретилось впервые
                            n=i     #сохраняем его индекс
                        elif 'F'and 'L'and 'A'and 'S'and 'H' in s[n:i+1]: #если уже есть число Фибоначчи и мы нашли второе
                            res=max(res,int(s[n]),int(s[i])) #максимальное из результирующей и двумя соседями
                            flag=False          #флаг опускаем, потому что строка уже хорошая, больше проверять не надо
                    else:res=max(res,int(s[i])) # строка уже хорошая и проверка просто на максимальное число Фибоначчи
                    # при этом проверяются все числа Фибоначчи во всех хороших строках

print(res)'''
