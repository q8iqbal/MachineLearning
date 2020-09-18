from .ConceptLearningBase import ConceptLearningBase


class CEleminator(ConceptLearningBase):
    __specific_hypothesis = ""
    __general_hypothesis = ""
    __result_hypothesis = []

    def __init__(self, data):
        super().__init__(data)
        self.__train(self.parsedData, self.parsedTarget)
        self.merge_hypothesis()

    def __train(self, data, target):
        for i, val in enumerate(target):
            if val == "Yes":
                self.__specific_hypothesis = data[i].copy()
                break
        data_length = len(self.__specific_hypothesis)
        self.__general_hypothesis = [["?" for i in range(data_length)] for i in range(data_length)]
        for i, val in enumerate(data):
            if target[i] == "Yes":
                for j in range(data_length):
                    if val[j] != self.__specific_hypothesis[j]:
                        self.__specific_hypothesis[j] = '?'
                        self.__general_hypothesis[j][j] = '?'
                    else:
                        continue
            else:
                for j in range(data_length):
                    if val[j] != self.__specific_hypothesis[j]:
                        self.__general_hypothesis[j][j] = self.__specific_hypothesis[j]
                    else:
                        self.__general_hypothesis[j][j] = '?'
        self.__clean_hypothesis()

    def __clean_hypothesis(self):
        false_data = ['?' for i in range(len(self.__specific_hypothesis))]
        count = 0
        for i, var in enumerate(self.__general_hypothesis):
            if var == false_data:
                count += 1

        for i in range(count):
            self.__general_hypothesis.remove(false_data)

    def merge_hypothesis(self):
        merger = []
        for i, val in enumerate(self.__specific_hypothesis):
            for j, val2 in enumerate(self.__general_hypothesis):
                if val in val2:
                    continue
                else:
                    temp = val2.copy()
                    temp[i] = val
                    merger.append(temp)
        for i in merger:
            if i not in self.__result_hypothesis:
                self.__result_hypothesis.append(i)

    def get_specific_hypothesis(self):
        return self.__specific_hypothesis

    def get_general_hypothesis(self):
        return self.__general_hypothesis

    def get_result(self):
        return self.__result_hypothesis
