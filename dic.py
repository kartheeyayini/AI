fruits={'orange': 10,'apple': 23,'grapes': [ 2 , 'violet', 90.8]}
print(fruits ['orange'])


veges={'carrot':'orange', 'beans' : 'peas' ,'coconut' : 'brown'}
print(veges['beans'])


my_colours={"pink": 45 , "lavander": 90}
print(my_colours["pink"])



my_list={'key1':'value1','key2':'value2'}

print(my_list['key1'])

my_foods={'biriyani':120,'chicken':40,'rice':[12,4.5,30],'fried ch':{'cookies':55,'samosa':70},'ginger':("hello foods"),'garlic':(89,9.00,784,"delicious")}
print(my_foods['fried ch'])
print(my_foods['rice'])

my_word={'word 1':'a','word 2':'banana'}
print(my_word)
word=my_word
print(word['word 1'].upper())
print('word 1'.upper())

karthika={'amma':'ramani','granny':'banu','thatha':'perumal'}
print(karthika['amma'])
print(karthika['amma'].upper(),karthika['granny'].upper(),karthika['thatha'].upper())
print(karthika['amma'].lower(),karthika['granny'].lower(),karthika['thatha'].lower())
print(karthika)
family=karthika
print(family)


letters={'A':['a','b','c']}
word=print(letters['A'][1])


digits={'w':[3,5,4]}
num=print(digits['w'][1:])

#d={'k1':122,'k2':144}
#print(d)
#print ( d ['k3']=300)
#print(d)


#tuples

tuple=(1,2,3)

type(tuple)

my_list=[1,2,3]
type(my_list)
len(my_list)

my_num=(1,"two",3,1,5,1,4,1)
print(my_num[1])
print(my_num.count(1))
print(my_num.index(5))
print(my_num[3])


#sets

colour=(1,1,1,1,2,3,4,5,5,5,4,4,4,4,4,4)
print(set(colour))

my_dic={"hello":5,"hi":(1,1,2,3,4), 4:[1,"good",7.9]}
print(my_dic)
print(my_dic["hi"])
print(set(my_dic["hi"]))

#i/o

print(my_file=open('python.txt'))
print(my_file.read())
print(my_file(open("C:\\Users\\Hello\\python.txt"))



with open('python.txt') as my_file:
    para=my_file.read()
    print(para)print(my_file=open('python.txt'))
print(my_file.read())
print(my_file(open("C:\\Users\\Hello\\python.txt"))



with open('python.txt') as my_file:
    para=my_file.read()
    print(para)

------------------------------
  car=open('my_life.txt','r')

print(car.read())
car.close()

f= open ('home.txt','+w')
print(f.write('hadsbh'))
print(f.close())

f= open ('home.txt','r')
print(f.read())
print(f.close())


#comp

x=5
y=9
print(x==y)

a=5.0
y=5
print(x==y)

----------------------------------

if,elseif,elif

my_score=100

if(my_score<500):
    print("good score")
else:
    print("improve")
    
my_name=False

if(my_name==True):
    
    print(my_name)
else:
    
    print("wrong")


class Testing:
    
    my_test_1=590
    my_test_2=900
    
    if(my_test_1+my_test_2!=2500):
        print('not equal')
    else:
        print('its equal')


        class Testing:
    
    my_test_1=590
    my_test_2=900
    
    if(my_test_1+my_test_2!=2500):
        print('not equal')
    else:
        print('its equal')
        
    my_test_3=[4,5,3,6,4]
    print(my_test_3[3])
    
    my_test_4={"producing":590,"developing":930,"procedure":[190,"level_1",679.80],"level_2":(123,"correction",56.7),"level_3":(1,1,1,2,2,2,3,3,3),"level_4":"opportunity"}
    print(my_test_4['producing'])
    print(set(my_test_4['level_3']))
    
    print(my_test_4["level_4"].upper())
    print(my_test_4['level_4'].lower())
    print(my_test_4["producing"])
    print(my_test_4["developing"])
    if (my_test_4["producing"]<3000):
        print("success")
    else:
        print("failed")
    
     if ((my_test_4["producing"])+(my_test_4["developing"])>3000):
        print("success")
    else:
        print("failed")

     if ((my_test_4["producing"])+(my_test_4["developing"])>3000):
        print("success")
    elif((my_test_4["producing"])+(my_test_4["developing"])<3000):
        print("running")
    else:
        print("failed")
    
    
    -----------------------

    for condition:

      class Testing_1:
    my_num=[167]
    for num in my_num:
        if num<100:
            print("enter")
        else:
            print("exit")


    my_num=[1,2,3,7,6,5,6,9]
    for num in my_num:
        if num%2==0:
            print('ok')
        else:
            print('no')

    my_level_1={"v1":33,"v2":22,'v3':76}
    for level_one in my_level_1:
        if (my_level_1["v1"]<40):
            print("equal")
        else:
            print("not equal")

          
    for level_one in my_level_1:
      print(level_one[1])
    for level_one in my_level_1.values():
        print(level_one)
    for level_one in my_level_1.items():
        print(level_one)

        