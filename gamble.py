import random

def gamble():
    if random.randint(0, 100) == 42:
        print("y  = 1,000,000,000,000,000,000,000,000")
        print("z  = 1,000,000,000,000,000,000,000")
        print("e  = 1,000,000,000,000,000,000")
        print("p  = 1,000,000,000,000,000")       
        print("t  = 1,000,000,000,000")    
        print("g  = 1,000,000,000") 
        print("m  = 1,000,000") 
        print("k  = 1,000")
        from slotmachine import SlotMachine
        from test import jackpots
        
    else:
        print("miss")

if __name__ == "__main__":
    while True:
        gamble()
        print('try again')