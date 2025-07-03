from tabulate import tabulate


class Operation:
    def __init__(self, headers):
        self.headers = headers

    def execute(self, rows):
        raise NotImplementedError

    def print(self, rows):
        print(tabulate(rows, headers=self.headers, tablefmt="grid", stralign="center"))
