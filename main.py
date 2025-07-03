import argparse
from operations.Aggregate_Operation import AggregateOperation
from operations.Filter_operation import FilterOperation
from operations.Base_operation import Operation
from Utils import Utils



def main():
    parser = argparse.ArgumentParser(description="Фильтрация и агрегация CSV с чанками")
    parser.add_argument("--file", required=True, help="CSV-файл")
    parser.add_argument("--where", help="Условие фильтрации, например: rating>4", action="append")
    parser.add_argument("--aggregate", help="Агрегация, например: rating=avg")
    args = parser.parse_args()

    headers = None
    all_filtered = []
    aggregator = None

    for hdrs, chunk in Utils.read_csv_in_chunks(args.file):
        if headers is None:
            headers = hdrs
        if args.aggregate:
            aggregator = AggregateOperation(headers, args.aggregate)
        
        if args.where:
            chunk = FilterOperation(headers, args.where).execute(chunk)

        if args.aggregate:
            aggregator.execute(chunk)
        else:
            all_filtered.extend(chunk)

    if args.aggregate:
        aggregator.print()
    else:
        Operation(headers).print(all_filtered)


if __name__ == "__main__":
    main()
