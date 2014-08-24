import json
import scipy.interpolate


class DummySpline:
    def __init__(self, values):
        self.value = values[0]
    def __call__(self, time):
        return self.value

class VectorSpline:
    def __init__(self, matrix, times):
        self.matrix = matrix
        self.times = times

        self.splines = []
        for parameterValues in self.matrix:
            if isinstance(parameterValues[0],
                    (int, long, float, complex)):
                spline = scipy.interpolate.UnivariateSpline(
                    self.times, parameterValues)
            else:
                spline = DummySpline(parameterValues)
            self.splines.append(spline)

    def __call__(self, time):

        #TODO: Make this pretty with a list comprehension
        returnValue = []
        for spline in self.splines:
            returnValue.append(spline(time))
        return returnValue

