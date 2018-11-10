#This is my Pokemon Store!
import datetime
from time import sleep
from random import randint
print ('Hello! Welcome to The Pokemon Shop!')
sleep(1)

user_money = 100
def coupons():
    pokedoll_coupons = 0
    return pokedoll_coupons

prices_pokeballs = {
    'Pokeball': 5,
    'Ultra Ball': 12,
    'Master Ball': 10000,
    'Premier Ball': 10,
    'Nest Ball': 15,
    'Timer Ball': 15,
    'Heal Ball': 50,
    'Great Ball': 10,
    'Luxary Ball': 20
    }
stock_pokeballs = {
    'Pokeball': 342,
    'Ultra Ball': 0,
    'Master Ball': 6,
    'Premier Ball': 58,
    'Nest Ball': 0,
    'Timer Ball': 211,
    'Heal Ball': 109,
    'Great Ball': 2,
    'Luxary Ball': 35,
    }

j = 'Darkrai'
j_fact = 'Darkrai\'s type is Dark!'
j_evolution = 'Darkrai doesn\'t have any evolutions.'
f = 'Pikachu'
f_fact = 'Pikachu\'s type is electric!'
f_evolution = 'It\'s the second evolution of Pichu, and it\'s third is Raichu!'
m = 'Celebi'
m_fact = 'Celebi\'s type is psychic and grass!'
m_evolution = 'Celebi doesn\'t have any evoutions.'
a = 'Deoxys'
a_fact = 'Deoxys\' type is psychic!'
a_evolution = 'Deoxys does not evolve, but can take 5 different forms!'
ma = 'Giratina'
ma_fact = 'Giratina\'s type is dragon and ghost!'
ma_evolution = 'Giratina does not evolve, but it can take 2 different forms!'
ju = 'Mimikyu'
ju_fact = 'Mimikyu is a ghost and fairy Pokemon, though other information is being discovered still!'
ju_evolution = 'Mimikyu has no known evolutions or other forms.'
jul = 'Snorlax'
jul_fact = 'Snorlax\'s type is normal.'
jul_evolution = 'Snorlax is the second evolution of Munchlax!'
au = 'Jirachi'
au_fact = 'Jirachi\'s type is psychic and steel!'
au_evolution = 'It does not take any other forms or evolutions.'
s = 'Phione'
s_fact = 'Phione is a water type Pokemon!'
s_evolution = 'Though Phione doesn\'t have any other evolutions, it can be bred through a Manaphy or another Phione.'
o = 'Lickytung'
o_fact = 'It\'s type is normal!'
o_evolution = 'It is the first evolution of Lickylicky!'
n = 'Meowth'
n_fact = 'Meowth\'s type is normal!'
n_evolution = 'It is the first evolution or Persian!'
d = 'Mew'
d_fact = 'Mew\'s type is psychic!'
d_evolution = 'Mew doesn\'t have any evolutions, but it is said to be related to Mewtwo!'

pokedolls = {
    'Mew',
    'Jigglypuff',
    'Snorlax',
    'Mimikyu',
    'Charmander'
    }

def pokeballs1():
    print('. . .')
    print ('Welcome to the Pokeball Section!')
    message = input('Would you like to see our prices? ')
    if message.lower() == 'yes':
        for item in prices_pokeballs:
            print (((item)+': ')+('$'+str(prices_pokeballs[item])))
    elif message.lower() == 'no':
        print ('Ah ok I see.')
    else:
        print ('It was a yes or no question!')
        return pokeballs1()
def pokeballs2():
    message2 = input('Would you like to see what we have in stock today? ')
    if message2.lower() == 'yes':
        for item in stock_pokeballs:
            print (((item)+': ')+(str(stock_pokeballs[item])))
        cart = []
        q1 = input('Would you like to add anything to your cart? ')
        if q1.lower() == 'yes':
            q2 = input('What would you like to add? ')
            cart.append(q2)
            print ('Your cart has: ')
            for item in cart:
                print (item)
        else:
            print ('Ok! Come back to Pokeballs soon :)')
    elif message2.lower() == 'no':
        print ('Ah ok I see.')
    else:
        print ('It was a yes or no question!')
        return pokeballs2()

def pokemon_monthly(month):
    print ('. . .')
    print ('Welcome to Pokemon Monthly!')
    sleep(1)
    print ('. . .')
    message_month2 = ('This month our famous pokemon is: ')
    if month == 1:
        print ('The month is January!')
        print ((message_month2)+(j)+'!')
        print (j_fact)
        print (j_evolution)
    if month == 2:
        print('The month is February!')
        print ((message_month2)+(f)+'!')
        print (f_fact)
        print (f_evolution)
    if month == 3:
        print ('The month is March!')
        print ((message_month2)+(m)+'!')
        print (m_fact)
        print (m_evolution)
    if month == 4:
        print ('The month is April!')
        print ((message_month2)+(a)+'!')
        print (a_fact)
        print (a_evolution)
    if month == 5:
        print ('The month is May!')
        print ((message_month2)+(ma)+'!')
        print (ma_fact)
        print (ma_evolution)
    if month == 6:
        print ('The month is June!')
        print ((message_month2)+(ju)+'!')
        print (ju_fact)
        print (ju_evolution)
    if month == 7:
        print ('The month is July!')
        print ((message_month2)+(jul)+'!')
        print (jul_fact)
        print (jul_evolution)
    if month == 8:
        print ('The month is August!')
        print ((message_month2)+(au)+'!')
        print (au_fact)
        print (au_evolution)
    if month == 9:
        print ('The month is September!')
        print ((message_month2)+(s)+'!')
        print (s_fact)
        print (s_evolution)
    if month == 10:
        print ('The month is October!')
        print ((message_month2)+(o)+'!')
        print (o_fact)
        print (o_evolution)
    if month == 11:
        print ('The month is November!')
        print ((message_month2)+(n)+'!')
        print (n_fact)
        print (n_evolution)
    if month == 12:
        print ('The month is December!')
        print ((message_month2)+(d)+'!')
        print (d_fact)
        print (d_evolution)

def pokequiz():
    correct = 0
    print ('. . .')
    print ('This is the Pokemon Quiz!')
    print ('You will answer 3 questions!')
    print ('. . .')
    sleep(1)
    print ('QUESTION 1')
    sleep(1)
    print ('What is not a region in the Pokemon world?')
    print ('a. Unova')
    print ('b. Johto')
    print ('c. Sinnoh')
    print ('d. Plento')
    a1 = input('Put your answer here: ')
    if a1 == 'd':
        print ('Correct!')
        correct += +1
    else:
        print ('Incorrect.')
    print ('. . .')
    sleep(1)
    print ('QUESTION 2')
    sleep(1)
    print ('A pokemon only goes up to level 99.')
    print ('a. True')
    print ('b. False')
    print ('c. Neither')
    a2 = input('Put your answer here: ')
    if a2 == 'b':
        print ('Correct!')
        correct += +1
    else:
        print ('Incorrect.')
    print ('. . .')
    sleep(1)
    print ('QUESTION 3')
    print ('Which Pokemon is a legendary?')
    print ('a. Rotom')
    print ('b. Snorlax')
    print ('c. Mew')
    print ('d. Phione')
    a3 = input('Put your answer here: ')
    if a3 == 'c':
        print ('Correct!')
        correct += +1
    else:
        print ('Incorrect.')
    print ('. . .')
    sleep(1)
    print ('You got '+str(correct)+' question(s) correct out of 3.')
    
def pokemon_guess():
    def user_guess():
        guess1 = int(input('Guess a number 1 through 10: '))
        return guess1
    print ('. . .')
    print ('Welcome to the Pokemon Guess game!')
    guess = user_guess()
    roll = randint(1,10)
    if guess > 10:
        print ('You\'re guess was too high!')
        return pokemon_guess()
    else:
        print ('Loading Number. . .')
        sleep(1)
        print (roll)
        sleep(1)
        if roll == guess:
            print ('You\'ve won!')
            print ('You get a free Pokemon Doll!')
            print ('So you may go to the Pokedoll shop and claim your prize!')
        elif roll != guess:
            print ('You\'ve lost.')
            def guess_again():
                message = input('Would you like to play again? ')
                if message == 'yes':
                    return pokemon_guess()
                elif message == 'no':
                    print ('Ok! Come back again soon!')
                else:
                    print ('It\'s a Yes or No question!')
                    return guess_again()
            guess_again()

def pokedoll():
    print ('. . .')
    sleep(1)
    print ('Hello! Welcome to the Pokedoll shop!')
    question = input('Would you like to see what we have? ')
    if question.lower() == 'yes':
        print ('Ok! We have:')
        sleep(1)
        for item in pokedolls:
            print (item)
        cart = []
        q1 = input('Would you like to add anything to your cart? ')
        if q1.lower() == 'yes':
            q2 = input('What would you like to add? ')
            cart.append(q2)
            print ('. . .')
            print ('Ok! Your cart has: ')
            for item in cart:
                print (item+' doll')
        elif q1.lower() == 'no':
            print ('Ok! Come back to Pokedolls soon :)')
        else:
            print ('That wasn\'t a yes or no!')
            return pokedoll()
    elif question.lower() == 'no':
        print ('Ah ok I see.')
    else:
        print ('That was not a yes or a no!')
        return pokedoll()

def end():
    print ('. . .')
    message2 = input('Is there anything else you would like to see? ')
    if message2 == 'yes':
        return step_1()
    elif message2 == 'no':
        print ('Ok! Have a good day, come back soon :)')
    else:
        print ('Please answer with Yes or No!')
        return end()
today = datetime.date.today()
def step_1():
    print ('. . .')
    print ('Our store has Pokeballs, Pokemon Monthly, Pokedolls, The Pokemon Quiz, and Pokemon Guess!')
    message = input('Which of our sections would you like to see? ')
    if message.lower() == 'pokeballs':
        pokeballs1()
        sleep(.5)
        pokeballs2()
        end()
    elif message.lower() == 'the pokemon quiz':
        pokequiz()
        end()
    elif message.lower() == 'pokedolls':
        pokedoll()
        end()
    elif message.lower() == 'pokemon monthly':
        pokemon_monthly(today.month)
        end()
    elif message.lower() == 'pokemon guess':
        pokemon_guess()
        end()
    else:
        print ('That is not on our list!')
        return step_1()

step_1()
outro = input('PRESS ENTER TO CLOSE')













