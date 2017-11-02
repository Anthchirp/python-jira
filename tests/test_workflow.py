import jiradls.workflow

def test_dls_workflow_status_dictionary():
  assert jiradls.workflow.status_name[4] == "analysis"
  assert jiradls.workflow.status_id["analysis"] == 4

def test_dls_workflow_known_transitions():
  assert 3 in jiradls.workflow.transitions[1]

def test_route_finding():
  # Open -> Active
  routes = jiradls.workflow.route_workflow(1, 3)
  assert routes == [ [1, 3],
                     [1, 2, 3],
                     [1, 7, 3],
                     [1, 2, 7, 3] ]

# import pprint
# pprint.pprint(routes)

  # Wait deploy -> In Progress
  routes = jiradls.workflow.route_workflow(9, 10)
  assert routes == [ [9, 8, 1, 10] ]

  # Open -> Resolved
  routes = jiradls.workflow.route_workflow(1, 7)
  assert routes[0] == [1, 7]
  assert len(routes) > 20

  # Open -> Resolved, avoiding Resolved
  routes = jiradls.workflow.route_workflow(1, 7, {7})
  assert routes == [ ]

  # Validation -> Open, not via Analysis or Development
  routes = jiradls.workflow.route_workflow(6, 1, {4, 5})
  assert routes == [ [6, 3, 2, 1],
                     [6, 7, 8, 1],
                     [6, 3, 7, 8, 1],
                     [6, 7, 3, 2, 1],
                     [6, 3, 2, 7, 8, 1] ]

