graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6 
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

node = find_lowest_cost_node(costs)
while node in not None:
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = find_lowest_cost_node
	processed.append(node)
	node = find_lowest_cost_node(costs)

def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[nodes]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return find_lowest_cost_node