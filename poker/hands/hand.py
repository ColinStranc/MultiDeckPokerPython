import poker.constants as constants

from poker.hands.optimality_evaluator import OptimalityEvaluator


class Hand:
    def __init__(self):
        self._cards = []

        self._optimality_evaluator = OptimalityEvaluator()
        (self.optimal_evaluation, self.showdown_hand) = self._optimality_evaluator.get_optimal_evaluation()

    def add_card(self, card):
        self._cards.append(card)
        (self.optimal_evaluation, self.showdown_hand) = self._optimality_evaluator.include_card(card)

    def to_string(self):
        if self._cards is []:
            return ""

        sb = "[ "
        for card in self._cards:
            sb += f"{card.to_string()} "
        sb += "]"

        return sb
