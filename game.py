gunzi = 21
while True:
    a = int(input('nideguishu1-4:'))
    if 4< a or a<1:
        print('cuole')
        continue
    if gunzi == 1:
       print("nishule")
       break
    print('diannoshu{}'.format(5-a))
    gunzi -= 5 
