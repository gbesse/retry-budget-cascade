import unittest
from retry_budget_cascade import run
class DomainTests(unittest.TestCase):
 def test_multiplicative_nested_retries(self):
  r=run({'root':'a','services':[{'id':'a','attempts':3,'calls':[{'service':'b'}]},{'id':'b','attempts':4,'calls':[{'service':'c','count':2}]},{'id':'c','attempts':5}]});self.assertEqual(r['worst_attempts_by_service'],{'a':3,'b':12,'c':120});self.assertEqual(r['worst_total_attempts'],135)
 def test_shared_dependency_counts_each_path(self):
  r=run({'root':'a','services':[{'id':'a','attempts':1,'calls':[{'service':'b'},{'service':'c'}]},{'id':'b','attempts':1,'calls':[{'service':'d'}]},{'id':'c','attempts':1,'calls':[{'service':'d'}]},{'id':'d','attempts':2}]});self.assertEqual(r['worst_attempts_by_service']['d'],4)
 def test_budget_upper_bound_not_claimed_enforced(self):
  r=run({'root':'a','shared_budget':2,'services':[{'id':'a','attempts':5}]});self.assertEqual(r['shared_budget_upper_bound'],2);self.assertTrue(r['budget_can_exhaust'])
 def test_no_retries_ratio_one(self):self.assertEqual(run({'root':'a','services':[{'id':'a','attempts':1}]})['amplification_ratio'],1)
 def test_cycles_rejected(self):
  with self.assertRaises(ValueError):run({'root':'a','services':[{'id':'a','attempts':1,'calls':[{'service':'a'}]}]})
