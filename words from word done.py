ask_word=input('Input a word: ').lower()
a=list(ask_word)
space=[' ','  ','   ']
List=['it','by','go','they','on','to','boom','boxer','lame','board','bit','board','game','rain','battery','at','pat','pit','come','shift','one','pill','kneel','off','of','time','gene','dim','heat','bear','dog','run','ten','tell','or','an','done','alt','wire','faith','key','low','lay']
for i in a:
    if i in space:
        a.remove(i)
        
    else:
        pass
from random import choice

b_list=[]
c_list=[]
d_list=[]
e_list=[]
f_list=[]
g_list=[]
h_list=[]
i_list=[]

for i in range(1,10000):
    b=choice(a)
    b_list.append(b)
    c=choice(a)
    c_list.append(c)
    d=choice(a)
    d_list.append(d)
    e=choice(a)
    e_list.append(e)
    f=choice(a)
    f_list.append(f)
    g=choice(a)
    g_list.append(g)
    h=choice(a)
    h_list.append(h)
    i=choice(a)
    i_list.append(i)

B=''.join(b_list)
C=''.join(c_list)
D=''.join(d_list)
E=''.join(e_list)
F=''.join(f_list)
G=''.join(g_list)
H=''.join(h_list)
I=''.join(i_list)

main_combination=B+C+D+E+F+G+H+I
main_list=[]
for j in List:
    if j in main_combination:
        main_list.append(j)
    else:
        pass
print('No words could be derived from the imputed word')



for u in main_list:
    print(u)
        
    

