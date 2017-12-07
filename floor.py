n = int(input("請輸入大樓的樓層數: "))
print ("本樓樓層為: ")
if ( n > 3 ):
    n += 1
for i in range( 1, n ):
    if ( i == 4 ):
       continue
    print( i, end =" " )
print()