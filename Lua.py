import math 
import random 
from math import ceil 
 
 
def F(bank_num):
    s1 = "" 
    s2 = "" 
    
    print("Введите номер банка:") 
    bank_num = int(input()) 
    
    s1 = list(str(bank_num))



    rand_num_BANK = random.randint(1_000_000_000, 9999999999) 
    s2 = list(str(rand_num_BANK)) 
    # print("Случайный номер в обратном порядке:")
    # print(*[i for i in reversed(s2)])
    # print(*[i for i in reversed(s1)]) 



    

    num_list1 = s1
    num_list2 = s2 
    
    # print(num_list1, num_list2) 

    
    list(str(num_list1)) 
    list(str(num_list2)) 



    joid = num_list1 + num_list2
    # print(joid)


    sum_chot = 0
    sum_nechot = 0 
    for bank_chislo_card in joid: 
        if int(bank_chislo_card) % 2 == 0: 
            sum_chot+=int(bank_chislo_card)
        if int(bank_chislo_card) % 2 != 0 and int(bank_chislo_card) < 10:
            sum_nechot+=int(bank_chislo_card)*2
        else:
            sum_nechot+=0


    # print("Сумма четных и не чётных чисел:", (sum_chot + sum_nechot)-2)
    print("Последняя цыфра карты:", abs(((sum_chot + sum_nechot)%10)-2))

    print("номер карты:")
    print(*[i for i in s1], *[i for i in s2], abs(((sum_chot + sum_nechot)%10)-2)) 


    return 0



F("bank_num")


