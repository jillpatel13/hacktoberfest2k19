n=int(input("Enter an integer:"))
print("Factors are:")
i=0
while n % 2 == 0: 
        print 2, 
        n = n / 2
for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
            while n % i== 0: 
                print i, 
                n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
  if n > 2: 
      print n 
