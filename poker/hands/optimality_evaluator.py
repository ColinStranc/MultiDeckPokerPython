import poker.constants as constants
import poker.hands.card as card


class OptimalityEvaluator:
    def __init__(self):
        self._cards = []

        self._evaluation = constants.NOT_COMPLETE
        self._showdown_hand = []

    def get_optimal_evaluation(self):
        return self._evaluation, self._showdown_hand

    def include_card(self, card):
        self._cards.append(card)

        if len(self._cards) < 5:
            self._evaluation = constants.NOT_COMPLETE
            self._showdown_hand = []
            return self.get_optimal_evaluation()

        self._evaluation = constants.NO_PAIR
        self._showdown_hand = self._cards

        return self.get_optimal_evaluation()
