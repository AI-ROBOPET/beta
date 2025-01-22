# base_agent.py
"""
Base class for AI Agents in the AI ROBOPET ecosystem.
"""

class BaseAgent:
    def __init__(self, name, abilities, owner_id):
        """
        Initialize a new AI agent.
        
        :param name: The name of the agent
        :param abilities: List of abilities the agent possesses
        :param owner_id: ID of the owner of the agent
        """
        self.name = name
        self.abilities = abilities
        self.owner_id = owner_id

    def get_details(self):
        """
        Retrieve the details of the agent.
        
        :return: Dictionary containing agent details
        """
        return {
            "name": self.name,
            "abilities": self.abilities,
            "owner_id": self.owner_id,
        }

    def add_ability(self, ability):
        """
        Add a new ability to the agent.
        
        :param ability: The ability to add
        """
        if ability not in self.abilities:
            self.abilities.append(ability)

    def remove_ability(self, ability):
        """
        Remove an ability from the agent.
        
        :param ability: The ability to remove
        """
        if ability in self.abilities:
            self.abilities.remove(ability)
