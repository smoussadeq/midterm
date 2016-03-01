# A credit card company computes a customer's "minimum payment" according to the following rule. The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is greater; however, if a $10 minimum payment exceeds the balance, then the minimum payment is the balance. Write a program to return the minimum payment. Assume that the variable balance contains the customer's balance.
#   Example 1: if your balance is 1000, then your program should return 21. 
#   Example 2: if your balance is 600, then your program should return 12.6. 
#   Example 3: if your balance is 25, then your program should return 10. 
#   Example 4: if your balance is 8, then your program should return 8. 

def computeMinimumPayment( balance ):
    #TODO write code inside this function that achieves the functionality described above
    if balance < 10:
        return balance
    elif balance > 10:
        return max(balance * 0.021, 10)