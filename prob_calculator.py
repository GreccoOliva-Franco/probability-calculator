import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **contentObject):
		self.contentObject = contentObject
		self.contents = self.set_content(contentObject)

	def set_content(self, contentObject):
		return [key for key in contentObject.keys() for iter in range(contentObject[key])]

	def draw(self, num):
		if num >= len(self.contents):
			return self.contents

		random.seed()
		return [self.contents.pop(random.randrange(0, len(self.contents))) for i in range(num)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	def isValid(actual, expect):
		validKey = 0
		for key, value in expect.items():
			if key in actual.keys() and actual[key] >= value:
				validKey += 1

		return validKey == len(expect)

	found = 0
	for iter in range(num_experiments):
		hatCopy = copy.deepcopy(hat)
		
		experiment = hatCopy.draw(num_balls_drawn)
		experiment.sort()
		experimentObject = {key: experiment.count(key) for key in tuple(experiment)}
		
		expected = [key for key in expected_balls.keys() for iter in range(expected_balls[key])]
		expectedObject = {key: expected.count(key) for key in tuple(expected)}
		expected.sort()

		if isValid(experimentObject, expectedObject):
			found += 1

	return found / num_experiments