import pandas as pd
import numpy as np


class ConceptLearningBase:

    def __init__(self, data):
        self.parsedData = ""
        self.parsedTarget = ""
        self.dataSet = self.__read_file(data)
        self.__parse_data(self.dataSet)

    def __read_file(self, data):
        data_set = pd.read_csv(data)
        return data_set

    def __parse_data(self, data_set):
        self.parsedData = np.array(data_set)[:, :-1]
        self.parsedTarget = np.array(data_set)[:, -1]

    def get_parsed_data(self):
        return self.parsedData

    def get_parsed_target(self):
        return self.parsedTarget
