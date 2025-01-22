# pet_agent.py
"""
Specialized class for AI ROBOPET agents, extending the BaseAgent class.
"""

from src.agents.base_agent import BaseAgent

class PetAgent(BaseAgent):
    def __init__(self, name, abilities, owner_id, pet_type):
        """
        Initialize a new AI ROBOPET agent.
        
        :param name: The name of the agent
        :param abilities: List of abilities the agent possesses
        :param owner_id: ID of the owner of the agent
        :param pet_type: Type of the pet (e.g., battle, support, explorer)
        """
        super().__init__(name, abilities, owner_id)
        self.pet_type = pet_type
        self.level = 1
        self.experience = 0

    def gain_experience(self, points):
        """
        Increase the agent's experience points and level up if applicable.
        
        :param points: Amount of experience to add
        """
        self.experience += points
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        """
        Increase the agent's level and reset experience points.
        """
        self.level += 1
        self.experience = 0
        print(f"{self.name} has leveled up to Level {self.level}!")

    def get_details(self):
        """
        Retrieve the details of the AI ROBOPET.
        
        :return: Dictionary containing agent details
        """
        details = super().get_details()
        details.update({
            "pet_type": self.pet_type,
            "level": self.level,
            "experience": self.experience,
        })
        return details

