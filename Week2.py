'''1) Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.'''

def intreverse(n):
    reverse = 0
    while (n > 0):
            Reminder = n % 10
            reverse = (reverse * 10) + Reminder
            n = n // 10
    return reverse



'''Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.'''

def matched(s):
    nesting = 0
    for i in s:
        if i == '(':
            nesting += 1
        elif i == ')':
            nesting -= 1
        if nesting < 0:
            return(False)
    return(nesting == 0)


'''Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.'''

def sumprimes(l):
   sum=0
   for i in l:
      if i>1:
         p=True
         for j in range(2,i):
            if(i%j==0):
                p=False
         if p:
            sum=sum+i
   return(sum)