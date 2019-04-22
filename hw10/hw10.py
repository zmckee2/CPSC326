def main():
    #adding one to each element in list
    list = [1,2,3,4,5]
    mapOp = lambda x : x + 1
    list2 = myMap(list, mapOp)
    print(list2)

    #appending Z to each element in list
    list = ['a','b','c','d','e']
    mapOp = lambda x : x + 'Z'
    list2 = myMap(list, mapOp)
    print(list2)

    #testing whether each element is even
    list = [1,2,3,4,5]
    mapOp = lambda x : x%2 == 0
    list2 = myMap(list, mapOp)
    print(list2)

def myMap(list, mapOp):
    retList = []
    for elm in list:
        retList.append(mapOp(elm))
    return retList

main()