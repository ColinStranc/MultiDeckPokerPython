import unittest
from poker.hands import hand_evaluation
from poker.hands.hand import Hand
import poker.hands.card as card
import poker.constants as constants


class TestHandEvaluation(unittest.TestCase):
    def test_empty_hand_evaluates_to_not_complete(self):
        empty_hand = Hand()
        evaluation = empty_hand.optimal_evaluation
        showdown_hand = empty_hand.showdown_hand

        self.assertEqual(constants.NOT_COMPLETE, evaluation, "Empty hand was evaluated as {0}".format(evaluation))
        self.assertEqual([], showdown_hand, "Empty hand contained a showdown hand")

    def test_hand_with_less_than_five_cards_evaluates_to_not_complete(self):
        incomplete_hand = Hand()

        incomplete_hand.add_card(card.C6)
        incomplete_hand.add_card(card.D2)
        incomplete_hand.add_card(card.H7)
        incomplete_hand.add_card(card.S3)

        evaluation = incomplete_hand.optimal_evaluation
        showdown_hand = incomplete_hand.showdown_hand

        self.assertEqual(constants.NOT_COMPLETE, evaluation, "Incomplete hand was evaluated as {0}".format(evaluation))
        self.assertEqual([], showdown_hand, "Incomplete hand contained showdown hand")

    def test_hand_evaluates_no_pair(self):
        no_pair_hand = Hand()

        cards_to_add = [card.C6, card.D2, card.H7, card.S3, card.SJ]
        for card_to_add in cards_to_add:
            no_pair_hand.add_card(card_to_add)

        evaluation = no_pair_hand.optimal_evaluation
        showdown_hand = no_pair_hand.showdown_hand

        self.assertEqual(constants.NO_PAIR, evaluation, f"Hand: {no_pair_hand.to_string()} evaluated to {evaluation}")
        self.assertEqual(5, len(showdown_hand), f"Showdown hand doesn't contain exactly 5 cards ({len(showdown_hand)})")

        for card_to_add in cards_to_add:
            self.assertTrue(showdown_hand.__contains__(card_to_add), f"{card_to_add.to_string()} not contained in "
                                                                     f"{no_pair_hand.to_string()}'s showdown hand")

    

    def test_ace_high_vs_8_high(self):
        ace_high_hand = Hand()
        ace_high_hand.add_card(card.C2)
        ace_high_hand.add_card(card.C6)
        ace_high_hand.add_card(card.D5)
        ace_high_hand.add_card(card.HJ)
        ace_high_hand.add_card(card.SA)

        eight_high_hand = Hand()
        eight_high_hand.add_card(card.S2)
        eight_high_hand.add_card(card.H3)
        eight_high_hand.add_card(card.D4)
        eight_high_hand.add_card(card.D5)
        eight_high_hand.add_card(card.C8)

        self.assertEqual(1, hand_evaluation.compare_hands(ace_high_hand, eight_high_hand))


