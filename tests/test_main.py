import pytest
import sys
from unittest.mock import patch, MagicMock
from main import main


@pytest.fixture
def sample_csv_chunk():
    headers = ["name", "brand", "price", "rating"]
    rows = [
        ["iPhone 15", "apple", "999", "4.9"],
        ["iPhone SE", "apple", "429", "4.1"],
        ["Galaxy S23", "samsung", "799", "4.5"]
    ]
    return headers, rows


def test_main_filter_only(sample_csv_chunk, monkeypatch):
    from main import Utils
    monkeypatch.setattr(Utils, "read_csv_in_chunks", lambda _: [sample_csv_chunk])

    mock_print = MagicMock()
    monkeypatch.setattr("main.Operation.print", mock_print)

    test_args = ["main.py", "--file", "dummy.csv", "--where", "brand=apple"]
    with patch.object(sys, 'argv', test_args):
        main()

    assert mock_print.called
    printed_rows = mock_print.call_args[0][0]
    assert len(printed_rows) == 2
    assert all(row[1] == "apple" for row in printed_rows)


def test_main_aggregation_only(sample_csv_chunk, monkeypatch):
    from main import Utils
    monkeypatch.setattr(Utils, "read_csv_in_chunks", lambda _: [sample_csv_chunk])

    mock_print = MagicMock()
    monkeypatch.setattr("main.AggregateOperation.print", mock_print)

    test_args = ["main.py", "--file", "dummy.csv", "--aggregate", "price=avg"]
    with patch.object(sys, 'argv', test_args):
        main()

    assert mock_print.called


def test_main_filter_and_aggregate(sample_csv_chunk, monkeypatch):
    from main import Utils
    monkeypatch.setattr(Utils, "read_csv_in_chunks", lambda _: [sample_csv_chunk])

    mock_print = MagicMock()
    monkeypatch.setattr("main.AggregateOperation.print", mock_print)

    test_args = ["main.py", "--file", "dummy.csv", "--where", "brand=apple", "--aggregate", "rating=avg"]
    with patch.object(sys, 'argv', test_args):
        main()

    assert mock_print.called


def test_main_invalid_aggregate(monkeypatch, sample_csv_chunk):
    from main import Utils
    monkeypatch.setattr(Utils, "read_csv_in_chunks", lambda _: [sample_csv_chunk])

    test_args = ["main.py", "--file", "dummy.csv", "--aggregate", "rating=unknown"]
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit):
            main()


def test_main_missing_column(monkeypatch, sample_csv_chunk):
    from main import Utils
    monkeypatch.setattr(Utils, "read_csv_in_chunks", lambda _: [sample_csv_chunk])

    test_args = ["main.py", "--file", "dummy.csv", "--where", "nonexistent=abc"]
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit):
            main()
