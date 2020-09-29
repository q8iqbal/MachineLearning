import math
import csv
import pandas as pd
import numpy as np

class KNearestNeighbor:
    ''''usia(0=muda, 1=paruh baya, 2=tua) berat(0=gemuk, 1=sangat gemuk, 2=terlalu gemuk)'''
    def __init__(self, data):
        self.__parse_data(self.__read_file(data))

    def __read_file(self, data):
        data_set = pd.read_csv(data)
        return data_set

    def __parse_data(self, data_set):
        self.parsedData = np.array(data_set)

    def get_parsed_data(self):
        return self.parsedData

    def __count_euclidean_distance(self, data1, data2, length):
        distance = 0
        for i in range(length):
            distance += pow((data1[i] - data2[i]), 2)
        return math.sqrt(distance)

    def __get_k_neighbor(self, input_data, k):
        distance = []
        length = len(input_data)
        for x in range(len(self.parsedData)):
            temp = self.__count_euclidean_distance(input_data, self.parsedData[x], length)
            distance.append((self.parsedData[x], temp))
        distance.sort(key=lambda x: x[1])
        neighbor = []
        for i in range(k):
            neighbor.append(distance[i][0])
        return neighbor

    def __get_response(self, neighbor):
        votes = {}
        for i in range(len(neighbor)):
            respone = neighbor[i][-1]
            if respone in votes:
                votes[respone] += 1
            else:
                votes[respone] = 1
        sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
        return sorted_votes[0][0]

    def _do_magic(self, input_data, k):
        ans = self.__get_response(self.__get_k_neighbor(input_data, k))
        return ans
