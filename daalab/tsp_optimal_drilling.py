import networkx as nx

def get_distances(num_nodes):
  distances={}
  for i in range(1,num_nodes+1):
    for j in range(i+1,num_nodes+1):
      distance=float(input(f"enter the distance between nodes{i} and node{j}:"))
      distances[(i,j)]=distance
      distances[(j,i)]=distance
  return distances

def tsp_optimal_drilling(distances):
  G=nx.Graph()
  G.add_weighted_edges_from((i,j,distances)for(i,j),distances in distances.items())
  optimal_length,optimal_order=nx.approximation.traveling_salesman_problem(G,cycle=True)
  return optimal_order

def calculate_optimal_cost(drill_order,distances):
  total_cost=sum(distances[(drill_order[i],drill_order[i+1])] for i in range(len(drill_order)-1))
  return total_cost

if __name__=="__main__":
  while True:
    num_nodes=int(input("enter the number of dril holes(nodes):"))
    distances=get_distances(num_nodes)
    
    optimal_order=tsp_optimal_drilling(distances)
    optimal_cost=calculate_optimal_cost(optimal_order,distances)
    print("optimal drilling order:",optimal_order)
    print(" Total optimal cost:",optimal_cost)
    try_again=input("do you want to try again with different number of nodes?(yes/no):").lower()
    if try_again !="yes":
      break
  
  '''
  Output:
  enter the number of dril holes(nodes):4
enter the distance between nodes1 and node2:2
enter the distance between nodes1 and node3:9
enter the distance between nodes1 and node4:10
enter the distance between nodes2 and node3:6
enter the distance between nodes2 and node4:4
enter the distance between nodes3 and node4:8
optimal drilling order: [1, 2, 3, 4, 2, 1]
 Total optimal cost: 22.0
do you want to try again with different number of nodes?(yes/no):no'''