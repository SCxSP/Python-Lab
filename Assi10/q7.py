class PropositionalKB:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def tell_fact(self, fact):
        self.facts.add(fact)

    def tell_rule(self, premises, conclusion):
        self.rules.append((set(premises), conclusion))

    def infer(self, query):
        inferred = set(self.facts)
        changed = True
        while changed:
            changed = False
            for premises, conclusion in self.rules:
                if premises.issubset(inferred) and conclusion not in inferred:
                    inferred.add(conclusion)
                    changed = True
        return query in inferred

kb = PropositionalKB()
kb.tell_fact("attends_class")
kb.tell_fact("submits_assignment")
kb.tell_rule(["attends_class", "submits_assignment"], "gets_grade_A")

print("KB Facts:", kb.facts)
q = input("Query proposition (e.g. gets_grade_A): ")
print("Inferred:", kb.infer(q))
