from __future__ import absolute_import, division, print_function

import jiradls.diamond


def test_issue_number_detection():
    # Numbers below 1000 are rejected
    assert jiradls.diamond.issue_number("1") == False
    assert jiradls.diamond.issue_number("12") == False
    assert jiradls.diamond.issue_number("123") == False

    # Numbers above 1000 are interpreted as SCI project
    assert jiradls.diamond.issue_number("1234") == "SCI-1234"

    # Non-numerical strings are rejected
    assert jiradls.diamond.issue_number("1234s") == False
    assert jiradls.diamond.issue_number("1s") == False

    # Accept issue names
    assert jiradls.diamond.issue_number("SCRATCH-1234") == "SCRATCH-1234"
    assert jiradls.diamond.issue_number("THING-1") == "THING-1"
    # Accept and change case
    assert jiradls.diamond.issue_number("i04_1-7") == "I04_1-7"

    # Reject invalid issue names
    assert jiradls.diamond.issue_number("SCRATCH-1234x") == False
    assert jiradls.diamond.issue_number("abc-def-1234") == False
    assert jiradls.diamond.issue_number("banana") == False

    # Other things
    assert jiradls.diamond.issue_number("") == False
    assert jiradls.diamond.issue_number(None) == False


def test_fixversion_filtering():
    candidate_versions = [
        "Run 1 (2019)",
        "Shutdown 1 (2019)",
        "Run 2 (2019)",
        "Shutdown 2 (2019)",
        "Diamond-DAWN 1.0",
        "Diamond-Dawn 1.1",
        "gda-8.30",
        "gda-8.32",
        "gda-8.34",
        "Dawn 1.5",
        "gda-8.36",
        "gda-8.38",
        "gda-8.40",
        "gda-8.42",
        "gda-8.44",
        "DAWN 1.8",
        "gda-8.46",
        "gda-8.48",
        "gda-8.50",
        "gda-8.52",
        "gda-9.0",
        "gda-9.1",
        "Dawn-1.9",
        "Dawn-1.10",
        "Dawn 2.0",
        "1.0",
        "Run 5 (2017)",
        "Shutdown 5 (2017)",
        "Run 1 (2018)",
        "Shutdown 1 (2018)",
        "Run 2 (2018)",
        "Shutdown 2 (2018)",
        "Run 3 (2018)",
        "Shutdown 3 (2018)",
        "Run 4 (2018)",
        "Shutdown 4 (2018)",
        "Run 5 (2018)",
        "Shutdown 5 (2018)",
    ]
    filtered_versions = jiradls.diamond.filter_versions(
        candidate_versions, run=2, year=2018
    )
    assert filtered_versions == [
        "Run 1 (2019)",
        "Shutdown 1 (2019)",
        "Run 2 (2019)",
        "Shutdown 2 (2019)",
        "Run 2 (2018)",
        "Shutdown 2 (2018)",
        "Run 3 (2018)",
        "Shutdown 3 (2018)",
        "Run 4 (2018)",
        "Shutdown 4 (2018)",
        "Run 5 (2018)",
        "Shutdown 5 (2018)",
    ]

    filtered_versions = jiradls.diamond.filter_versions(
        candidate_versions, run=5, year=2017, return_map=True
    )
    assert filtered_versions == {
        "run1": "Run 1 (2018)",
        "run2": "Run 2 (2018)",
        "run3": "Run 3 (2018)",
        "run4": "Run 4 (2018)",
        "run5": "Run 5 (2017)",
        "shutdown1": "Shutdown 1 (2018)",
        "shutdown2": "Shutdown 2 (2018)",
        "shutdown3": "Shutdown 3 (2018)",
        "shutdown4": "Shutdown 4 (2018)",
        "shutdown5": "Shutdown 5 (2017)",
    }
