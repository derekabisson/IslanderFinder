from graph import Graph

test1 = [
    [0,0,1,0,0],
    [1,0,0,0,0],
    [1,0,0,1,1],
    [0,0,0,1,1],
]

test2 = [
    [0,0,0,0,0,0,0],
    [1,1,0,0,1,1,0],
    [1,0,0,0,0,0,0],
    [0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0]
]
test3 = [
    [1,0,0,0,1,1,0],
    [0,0,1,0,0,0,0],
    [1,0,1,0,0,0,0],
    [1,0,0,0,1,1,0],
    [0,0,1,0,0,0,0],
]

test4 = [
    [1,1,1,0,0,0,0],
    [0,1,1,0,0,0,0],
    [0,0,1,0,0,1,1],
    [1,1,1,0,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0]
]

gr1 = Graph(test1)
print("Find Islands for map 1")
gr1.find_islands()

gr2 = Graph(test2)
print("Find Islands for map 2")
gr2.find_islands()

gr3 = Graph(test3)
print("Find Islands for map 3")
gr3.find_islands()

gr4 = Graph(test4)
print("Find Islands for map 4")
gr4.find_islands()