class BudgetList:
    def __init__(self,budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = 0
        self.overages = []

    def append(self,item):
        if(self.sum_expenses+item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item




