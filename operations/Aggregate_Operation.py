import sys
from operations.Base_operation import Operation
from tabulate import tabulate


class AggregateOperation(Operation):
    def __init__(self, headers, agg_expr):
        super().__init__(headers)
        self.func, self.col = self.parse_agg(agg_expr)
        self.values = []

    def parse_agg(self, expr):
        parts = expr.split("=")
        if len(parts) != 2:
            sys.exit("Неверный формат агрегации. Пример: rating=avg")
        col = parts[0].strip()
        func = parts[1].strip().lower()
        if func not in {"avg", "min", "max"}:
            sys.exit(f"Неизвестная функция агрегации: {func}")
        return func, col

    def execute(self, rows):
        if self.col not in self.headers:
            sys.exit(f"Колонка '{self.col}' не найдена")

        col_idx = self.headers.index(self.col)
        for row in rows:
            try:
                self.values.append(float(row[col_idx]))
            except (ValueError, IndexError):
                continue

    def print(self):
        if not self.values:
            result = None
        else:
            match self.func:
                case "avg":
                    result = sum(self.values) / len(self.values)
                case "min":
                    result = min(self.values)
                case "max":
                    result = max(self.values)
        print(
            tabulate(
                [[result]], headers=[self.func], tablefmt="grid", stralign="center"
            )
        )
