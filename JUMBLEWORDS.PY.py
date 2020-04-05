# JUMBLE WORDS GAME IN WHICH TWO PLAYER CAN PLAY SIMULTANEOUSLY. You have to think and make meaningful words.
print("""
                         Welcome to coder2hacker Joy of Computing Using Python
                                       Let's Play 
                                       Brain Game
""")
import random
def choose():
    c=['computer','nursing','management','science','Python','Dictionary','chitkara']
    pick= random.choice(c)
    return pick
def jumbled(word):
    jumble="".join(random.sample(word,len(word)))
    return jumble
def play():
    p1n = input("Enter Player1 Name:-")
    p2n = input('Enter player2 Name:-')
    p1s,p2s=0,0
    turn=0
    while 1:
        pick =choose()
        word= jumbled(pick)
        print(word)
        if turn%2==0:
            print(p1n, "It's your turn")
            inp=input('Enter your answer')
            if inp==pick:
                print('Well done Guess is corect!')
                p1s = p1s+1
                print('Your score is:- ',p1s)
            else:
                print('Better luck',pick)
                print('Your score is:-',p1s)
            con = int(input("Press '1' to continue '0' to exit:-"))
            if con==0:
                print("Well played ", p1n,p1n)
                print("Player1 Score is:-",p1s,"Player2 score is:-",p2s)
                break
        else:
            print(p2n, "It's your turn")
            inp = input('Enter your answer')
            if inp ==pick:
                print('Chicken dinner PUBG')
                p2s = p2s + 1
                print('Your score is:- ', p2s)
            else:
                print('Better luck', pick)
                print('Your score is:-', p2s)
            con=int(input("Press '1' to continue '0' to exit:-"))
            if con == 0:
                print("Well played ", p1n, p1n)
                print("Player1 Score is:-", p1s, "Player2 score is:-", p2s)
                break
        turn = turn +1
play()

print("""Thanks for Playing!!! """)
