import math


def count_euclidean_distance( data1, data2, length):
    distance = 0
    for i in range(length):
        distance += pow((data1[i] - data2[i]), 2)
    return math.sqrt(distance)

def get_k_neighbor(parsedData, input_data, k):
    distance = []
    length = len(input_data) - 1
    for x in range(len(parsedData)):
        temp = count_euclidean_distance(input_data, parsedData[x], length)
        distance.append((parsedData, temp))
    distance.sort(key=lambda x: x[1])
    neighbor = []
    for i in range(k):
        neighbor.append(distance[x][0])
    return neighbor

trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
testInstance = [5, 5, 5]
k = 1
neighbors = get_k_neighbor(trainSet, testInstance, k=1)
print(neighbors)