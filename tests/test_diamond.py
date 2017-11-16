from __future__ import absolute_import, division, print_function

import jiradls.diamond

def test_issue_number_detection():
  # Numbers below 1000 are rejected
  assert jiradls.diamond.issue_number('1') == False
  assert jiradls.diamond.issue_number('12') == False
  assert jiradls.diamond.issue_number('123') == False

  # Numbers above 1000 are interpreted as SCI project
  assert jiradls.diamond.issue_number('1234') == 'SCI-1234'

  # Non-numerical strings are rejected
  assert jiradls.diamond.issue_number('1234s') == False
  assert jiradls.diamond.issue_number('1s') == False

  # Accept issue names
  assert jiradls.diamond.issue_number('SCRATCH-1234') == 'SCRATCH-1234'
  assert jiradls.diamond.issue_number('THING-1') == 'THING-1'
  # Accept and change case
  assert jiradls.diamond.issue_number('i04_1-7') == 'I04_1-7'

  # Reject invalid issue names
  assert jiradls.diamond.issue_number('SCRATCH-1234x') == False
  assert jiradls.diamond.issue_number('abc-def-1234') == False
  assert jiradls.diamond.issue_number('banana') == False

  # Other things
  assert jiradls.diamond.issue_number('') == False
  assert jiradls.diamond.issue_number(None) == False
