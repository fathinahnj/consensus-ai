# src/core/agent.py

class Agent:
    """
    Static attributes 
    """

    def __init__(self, agent_id: int, attributes: dict):
        self.id = agent_id

        # ------------------------------------------------------------------
        # Static states
        # ------------------------------------------------------------------
        self.age_group = attributes.get("age_group")
        self.education_level = attributes.get("education_level")
        self.income_level = attributes.get("income_level")
        
        self.digital_exposure = attributes.get("digital_exposure")
        
        self.cognitive_complexity = attributes.get("cognitive_complexity")
        self.issue_based_reasoning = attributes.get("issue_based_reasoning")
        self.authority_deference = attributes.get("authority_deference")

        self.economic_anxiety = attributes.get("economic_anxiety")
        self.welfare_salience = attributes.get("welfare_salience")
        self.status_quo_bias = attributes.get("status_quo_bias")
