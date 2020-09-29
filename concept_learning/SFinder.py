from .ConceptLearningBase import ConceptLearningBase


class SFinder(ConceptLearningBase):
    """class for ML find S algorithm"""
    __result_hypothesis = ""

    def __init__(self, data):
        super().__init__(data)
        self._result_hypothesis = self.__train(self.parsedData, self.parsedTarget)

    def __train(self, data, target):
        first_hypothesis = 0
        for i, val in enumerate(target):
            if val == "Yes":
                first_hypothesis = data[i].copy()
                break
        for i, val in enumerate(data):
            if target[i] == "Yes":
                for j in range(len(first_hypothesis)):
                    if val[j] != first_hypothesis[j]:
                        first_hypothesis[j] = '?'
                    else:
                        continue
        return first_hypothesis

    def get_result(self):
        return self._result_hypothesis
