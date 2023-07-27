def knapsack_max_profit(weight,costs,capacity):
    num_items=len(weight)
    #create a table to store the max profits for different capacitites
    table=[[0]*(capacity+1) for _ in range(num_items+1)]
    #fill in the table using dynamic programming
    for i in range(1,num_items+1):
        for j in range(1,capacity+1):
            #if the current item's weight is less than or equal to the current capacity
            if weight[i-1] <=j:
                #consider the maximum profit by either including or excluding the current item
                table[i][j]=max(costs[i-1]+table[i-1][j-weight[i-1]],table[i-1][j])
            else:
                #if the current items weight is greater than the current capacity,exclude it
                table[i][j]=table[i-1][j]
    #trace back through the table to find the items that contribute to the maximum profit
    selected_items = []
    total_weights = capacity
    for i in range(num_items,0,-1):
           if table[i] [total_weights] !=table[i-1][total_weights]:
              selected_items.append(i-1)
              total_weights -=weight[i-1]
              
    #return the maximum profit and the selected items
    return table[num_items][capacity], selected_items 

#example usage
#weight=[2,3,4,5] #weights of the coffee beans types
#costs=[10,20,30,40] #costs of the coffee bean types
#capacity=10 # maximum weight capacity of the bag

weight = input("Enter the weights of the items (comma-separated): ")
weight = [int(w) for w in weight.split(",")]
costs = input("Enter the costs of the items (comma-separated): ")
costs = [int(c) for c in costs.split(",")]
capacity = int(input("Enter the capacity of the knapsack: "))

max_profit,selected_items=knapsack_max_profit(weight,costs,capacity) 
print("Maximum Profits: ",max_profit)
print("Selected Coffee Beans[index]:",selected_items)
print("Selected Coffee Beans[weight]:",[weight[i] for i in selected_items])
print("Selected Cofee Beans[costs]:",[costs[i] for i in selected_items]) 

'''
Output:
Maximum Profits:  70
Selected Coffee Beans[index]: [3, 1, 0]
Selected Coffee Beans[weight]: [5, 3, 2]
Selected Cofee Beans[costs]: [40, 20, 10]

-----------OR-----------

Enter the weights of the items (comma-separated): 2,3,4,5
Enter the costs of the items (comma-separated): 10,20,30,40
Enter the capacity of the knapsack: 10
Maximum Profits:  70
Selected Coffee Beans[index]: [3, 1, 0]
Selected Coffee Beans[weight]: [5, 3, 2]
Selected Cofee Beans[costs]: [40, 20, 10]'''
   