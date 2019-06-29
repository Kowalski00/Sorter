'''
Created on 23 de mai de 2018

A sorter program

@author: Kowalski, R
'''
import random

def check(c_list):
    i = 0
    len_list = len(c_list)
    var_check = c_list[0]
    while i < len_list:
        if var_check > c_list[i]:
            return False
        var_check = c_list[i]
        i+=1
    return True

def gen_list(size):
    i = 0
    g_list = []
    while i<size: 
        rdn_number = random.randint(0,100)
        g_list.append(rdn_number)
        i += 1
    return g_list

def bubble(b_list):
    i = 0
    list_len = len(b_list)
    var = b_list[0]
    while i < list_len:
        if var > b_list[i]:
            b_list[i-1] = b_list[i]
            b_list[i] = var
            var = b_list[i]
            
        else:
            var = b_list[i]
        i+=1
        
    return b_list

def merge(m_list):
    middleLen = len(m_list)//2
    
    list_1 = m_list[:middleLen]
    list_2 = m_list[middleLen:]
    
    
    if len(list_1)>1:
        merge(list_1)
        
    if len(list_2)>1:
        merge(list_2)
        
    i=0
    j=0
    k=0
    
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            m_list[k] = list_1[i]
            i+=1
        else:
            m_list[k] = list_2[j]
            j+=1
        k+=1
        
    while i < len(list_1):
        m_list[k] = list_1[i]
        i+=1
        k+=1
    while j < len(list_2):
        m_list[k] = list_2[j]
        j+=1
        k+=1
    return m_list
        


def selection(s_list):
    i = 0
    s_list2 = []
    len_list = len(s_list)
    while i < len_list:
        min_number = min(s_list)
        s_list.remove(min_number)
        s_list2.append(min_number)
        i += 1
    return s_list2

while True:
    list_size = int(input('\nChoose the size of your randomly-generated list: '))
    list = gen_list(list_size)
    print(list)
    counter = 0
    cmd = input('\nFrom the list: \nBubble, Merge, Selection \nChoose your sorter: ')
    if cmd == 'bubble':
        chk = check(list)
        while chk == False:
            list = bubble(list)
            chk = check(list)
            counter+=1
        print(list, 'number of iterations: ', counter)
    
    if cmd == 'merge':
        list = merge(list)
        print(list)
        #print('https://pt.wikipedia.org/wiki/Merge_sort')
    
    if cmd == 'selection':
        list = selection(list)
        print(list)
