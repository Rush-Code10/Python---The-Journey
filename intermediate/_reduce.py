from functools import reduce
expenses_1 = [('Dinner',120),('Car Wash',250)]
sum = reduce(lambda a,b : a[1] + b[1] , expenses_1)
print(expenses_1,sum)


expenses_2 = [('Dinner',120),('Car Wash',250),('Habibi',130)]
total_expenses = reduce(lambda x, y: x + y[1], expenses_2, 0)

print(expenses_2,total_expenses) # Output: 500

'''
This code performs the following operations:

It defines a list of tuples named expenses_2 which contains the names and costs of different expenses, 
such as dinner, car wash, and Habibi.

It then uses the reduce function from the functools module to calculate the total cost of all expenses. 
The reduce function takes three arguments: a function, an iterable (in this case, expenses_2), and an initial 
value (in this case, 0).

The lambda function passed to reduce takes two arguments, x and y. The x represents the accumulated value of the 
previous calculation and y represents the current element being iterated over, which is a tuple containing the name 
and cost of an expense.

In each iteration, the lambda function adds the second element of the current tuple (which represents the cost of 
an expense) to the accumulated value (x) from the previous iteration.

Finally, the result of reduce is assigned to total_expenses, which contains the total cost of all expenses.

The code then prints out the original expenses_2 list and the total expenses, which is 500 in this case.
'''