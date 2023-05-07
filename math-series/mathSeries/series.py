def fibonacci(n):
     '''  This function calculate the Fibonacci for integer
        parameter n and return the result
        
     '''
     if n == 0:
        return 0
     elif n == 1:
        return 1
     else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
     '''  This function calculate the Lacus for integer
        parameter n and return the result
        
     '''
     if n == 0:
        return 2
     elif n == 1:
        return 1
     else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, first, second):
         '''  This function calculate the summation series for integer
             parameter n / first / second and return the result
                '''
         if(first==0 and second==1):
           return fibonacci(n)
         elif (first==2 and second==1):
            return lucas(n)
         else:
           return sum_series(n-1, first, second) + sum_series(n-2, first, second)
        

if __name__ == "__main__":
    print(fibonacci(9))
    print(lucas(8))
    print(sum_series(4,0,1))
