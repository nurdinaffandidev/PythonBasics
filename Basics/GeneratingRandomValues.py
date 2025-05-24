import random
for i in range(3):
    # print(random.random())
    print(random.randint(10,20))

members = ["John", "Mary", "Bob", "Moss"]
leader = random.choice(members)
print(leader)

class Dice:
    @staticmethod
    def roll():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        return dice1, dice2


dice = Dice()
print(dice.roll()) # using instance
print(Dice.roll()) # with @staticmethod