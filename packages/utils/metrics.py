class Metrics:
    def __init__(self):
        self.data = {}
    def add_metric(self, name, value):
        self.data[name] = value
metrics = Metrics()