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
        
        # ------------------------------------------------------------------
        # Dynamic states 
        # ------------------------------------------------------------------
        self.opinion = attributes.get("initial_opinion", self.ideology_prior)
        self.confidence = attributes.get("initial_confidence", 0.5) 
        
        # ------------------------------------------------------------------
        # Interaction states 
        # ------------------------------------------------------------------
        # self.vote_intention = None
        self.times_spoken = 0
        self.influence_exerted = 0.0
        
    # ------------------------------------------------------------------
    # Minimal helper methods 
    # ------------------------------------------------------------------

    def speak(self):
        """
        Mark that the agent has spoken in a discussion round.
        """
        self.times_spoken += 1
        
    def record_influence(self, magnitude: float):
        """
        Record the influence exerted by this agent.
        """
        self.influence_exerted += abs(magnitude)
        
    # ------------------------------------------------------------------
    # Snapshot for logging / analysis
    # ------------------------------------------------------------------

    def snapshot(self) -> dict:
        return {
            "id": self.id,
            "opinion": self.opinion,
            "confidence": self.confidence,
            "age_group": self.age_group,
            "education_level": self.education_level,
            "income_level": self.income_level,
            "times_spoken": self.times_spoken,
            "influence_exerted": self.influence_exerted,
        }