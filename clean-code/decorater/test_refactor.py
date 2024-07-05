from refactor import process_data, analyze_data, report_data
import pytest

def test_process_data():
    assert process_data(10) == 20
    with pytest.raises(ValueError):
        process_data(-10)

def test_analyze_data():
    assert analyze_data(10) == 5.0
    with pytest.raises(ValueError):
        analyze_data(-10)

def test_report_data():
    assert report_data(10) == "Report: 10"
    with pytest.raises(ValueError):
        report_data(-10)