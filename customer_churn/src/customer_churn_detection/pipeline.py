class Pipeline:
    def __init__(self, steps):
        self._steps = steps

    def run(self, data):
        for step in self._steps:
            data = step.run(data)

        return data