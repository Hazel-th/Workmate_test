import sys
from operations.Base_operation import Operation


class FilterOperation(Operation):
    def __init__(self, headers, conditions):
        super().__init__(headers)
        self.operation_parse = self.parse_conditions(conditions)

    @staticmethod
    def cast_value(val):
        try:
            if "." in val:
                return float(val)
            return int(val)
        except ValueError:
            return val

    def parse_conditions(self, conditions):
        res = []
        for op in [">=", "<=", ">", "<", "="]:
            for condition in conditions:
                if op in condition:
                    parts = condition.split(op)
                    if len(parts) != 2:
                        sys.exit(f"Неверный формат условия: {condition}")
                    res.append([parts[0].strip(), op, parts[1].strip()])
        if not res:
            sys.exit(f"Не найден оператор в условии: {conditions}")
        return res

    def compare(self, cell, op, val):
        cell_val = self.cast_value(cell)
        val_casted = self.cast_value(val)

        match op:
            case ">":
                return cell_val > val_casted
            case "<":
                return cell_val < val_casted
            case "=":
                return cell_val == val_casted
            case ">=":
                return cell_val >= val_casted
            case "<=":
                return cell_val <= val_casted
            case _:
                sys.exit(f"Неизвестный оператор: {op}")

    def execute(self, rows):
        for col, _, _ in self.operation_parse:
            if col not in self.headers:
                sys.exit(f"Колонка '{col}' не найдена в заголовках {self.headers}")

        filtered_rows = []
        for row in rows:
            if all(
                self.compare(row[self.headers.index(col)], op, val)
                for col, op, val in self.operation_parse
            ):
                filtered_rows.append(row)
        return filtered_rows
