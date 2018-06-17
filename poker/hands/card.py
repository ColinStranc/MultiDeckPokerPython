import poker.constants as c


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def to_string(self):
        return f"{self.value}{self.suit}"


C2 = Card(c.CLUB, c.TWO)
C3 = Card(c.CLUB, c.THREE)
C4 = Card(c.CLUB, c.FOUR)
C5 = Card(c.CLUB, c.FIVE)
C6 = Card(c.CLUB, c.SIX)
C7 = Card(c.CLUB, c.SEVEN)
C8 = Card(c.CLUB, c.EIGHT)
C9 = Card(c.CLUB, c.NINE)
CT = Card(c.CLUB, c.TEN)
CJ = Card(c.CLUB, c.JACK)
CQ = Card(c.CLUB, c.QUEEN)
CK = Card(c.CLUB, c.KING)
CA = Card(c.CLUB, c.ACE)

D2 = Card(c.DIAMOND, c.TWO)
D3 = Card(c.DIAMOND, c.THREE)
D4 = Card(c.DIAMOND, c.FOUR)
D5 = Card(c.DIAMOND, c.FIVE)
D6 = Card(c.DIAMOND, c.SIX)
D7 = Card(c.DIAMOND, c.SEVEN)
D8 = Card(c.DIAMOND, c.EIGHT)
D9 = Card(c.DIAMOND, c.NINE)
DT = Card(c.DIAMOND, c.TEN)
DJ = Card(c.DIAMOND, c.JACK)
DQ = Card(c.DIAMOND, c.QUEEN)
DK = Card(c.DIAMOND, c.KING)
DA = Card(c.DIAMOND, c.ACE)

H2 = Card(c.HEART, c.TWO)
H3 = Card(c.HEART, c.THREE)
H4 = Card(c.HEART, c.FOUR)
H5 = Card(c.HEART, c.FIVE)
H6 = Card(c.HEART, c.SIX)
H7 = Card(c.HEART, c.SEVEN)
H8 = Card(c.HEART, c.EIGHT)
H9 = Card(c.HEART, c.NINE)
HT = Card(c.HEART, c.TEN)
HJ = Card(c.HEART, c.JACK)
HQ = Card(c.HEART, c.QUEEN)
HK = Card(c.HEART, c.KING)
HA = Card(c.HEART, c.ACE)

S2 = Card(c.SPADE, c.TWO)
S3 = Card(c.SPADE, c.THREE)
S4 = Card(c.SPADE, c.FOUR)
S5 = Card(c.SPADE, c.FIVE)
S6 = Card(c.SPADE, c.SIX)
S7 = Card(c.SPADE, c.SEVEN)
S8 = Card(c.SPADE, c.EIGHT)
S9 = Card(c.SPADE, c.NINE)
ST = Card(c.SPADE, c.TEN)
SJ = Card(c.SPADE, c.JACK)
SQ = Card(c.SPADE, c.QUEEN)
SK = Card(c.SPADE, c.KING)
SA = Card(c.SPADE, c.ACE)
