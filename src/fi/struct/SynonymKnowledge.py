class SynonymKnowledge:
    def __init__(self, knowledge: dict):
        self.knowledge = knowledge

    def getLHS(self, rhs: str): return self.knowledge[rhs]

    def __str__(self):
        return "${len(self.knowledge)} items"