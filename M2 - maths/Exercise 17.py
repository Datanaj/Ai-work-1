#### Exercise 17: which is the probability of drawing a heart or an ace?

# there are 13/52 cards that are hearts.
# 4 out of 52 cards are aces so to test for both of these is 17/52
p_ace = 4/52
p_hearts = 13/52
p_hearts_or_ace = p_ace + p_hearts
print(p_hearts_or_ace)