d = {1: ["FastEthernet0/0", '192.168.1.242', 'YES','manual up','  up'],
2: ["FastEthernet1/0", 'unassigned', 'YES','unset','      down'],
3: ["Serial2/0  ", '  192.168.1.250', 'YES','manual up','  up'],
10: ["Serial3/0  ", '  192.168.1.233', 'YES','manual up','  up'],
5: ["FastEthernet4/0", 'unassigned  ', 'YES','unset','     down'],
6: ["FastEthernet5/0", 'unassigned  ', 'YES','unset','     down'] }
print ("Pos,  Interface     ,     IP-Address      ,  OK?     ,  Method Status    ,  Protocol")
for k, v in d.items():    

    lang, perc, change, abc, defghi = v
    print (k, "  ", lang, "    ", perc, "     ",  change, "    ", abc, "        ", defghi)


def func(abc):
    print(type(abc))
    for i in abc:
        print(abc[i][1],"/",abc[i][3])

func(d)