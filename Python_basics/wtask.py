

secret_number = 7

while True :
    number=int(input("To guess the secret number :"))
    
    if number==secret_number:
        print("correct you guessed it..!")
        break
    else:
     print("wrong number plz try again..!")
     

