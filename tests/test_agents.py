# test_agents.py
"""
Unit tests for AI ROBOPET agents.
"""

import unittest
from src.agents.base_agent import BaseAgent
from src.agents.pet_agent import PetAgent

class TestBaseAgent(unittest.TestCase):
    def setUp(self):
        self.base_agent = BaseAgent(name="TestAgent", abilities=["shield"], owner_id="user123")

    def test_get_details(self):
        details = self.base_agent.get_details()
        self.assertEqual(details["name"], "TestAgent")
        self.assertEqual(details["abilities"], ["shield"])
        self.assertEqual(details["owner_id"], "user123")

    def test_add_ability(self):
        self.base_agent.add_ability("laser")
        self.assertIn("laser", self.base_agent.abilities)

    def test_remove_ability(self):
        self.base_agent.remove_ability("shield")
        self.assertNotIn("shield", self.base_agent.abilities)

class TestPetAgent(unittest.TestCase):
    def setUp(self):
        self.pet_agent = PetAgent(name="RoboMax", abilities=["laser"], owner_id="user456", pet_type="battle")

    def test_get_details(self):
        details = self.pet_agent.get_details()
        self.assertEqual(details["name"], "RoboMax")
        self.assertEqual(details["pet_type"], "battle")
        self.assertEqual(details["level"], 1)
        self.assertEqual(details["experience"], 0)

    def test_gain_experience(self):
        self.pet_agent.gain_experience(120)
        self.assertEqual(self.pet_agent.level, 2)
        self.assertEqual(self.pet_agent.experience, 0)

if __name__ == "__main__":
    unittest.main()
