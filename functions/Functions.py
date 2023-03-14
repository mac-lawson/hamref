from colorama import Fore

def LogQSO(call, date, freq, location):
    # Open the file in append mode
    with open("./data/QSO.txt", "a") as file:
        
        # Append a new line character to the end of the file
        file.write("\n")
        
        # Write the new line of text to the next free line
        file.write("[QSO Log] Call: " + str(call) + " | Date: " + str(date) + " | Frequency/Band: " + str(freq) + " | Grid: " + str(location))
def getQSOs():
    print(Fore.LIGHTCYAN_EX)
    qsos = open("./data/QSO.txt")

    print(qsos.read())
    print("\n")
    print(Fore.LIGHTBLUE_EX)  

def hamQRF():
    print("\n" + Fore.LIGHTGREEN_EX)
    print("{:^60}".format("HAM RADIO QUICK REFERENCE"))
    print("-" * 60)
    print("{:<20} {:<20} {:<20}".format("FREQUENCY", "BAND", "MODE"))
    print("{:<20} {:<20} {:<20}".format("3.5 - 4.0 MHz", "80m", "CW/SSB"))
    print("{:<20} {:<20} {:<20}".format("7.0 - 7.3 MHz", "40m", "CW/SSB"))
    print("{:<20} {:<20} {:<20}".format("14.0 - 14.35 MHz", "20m", "CW/SSB"))
    print("{:<20} {:<20} {:<20}".format("21.0 - 21.45 MHz", "15m", "CW/SSB"))
    print("{:<20} {:<20} {:<20}".format("28.0 - 29.7 MHz", "10m", "CW/SSB/FM"))
    print("-" * 60)
    print("{:<20} {:<20} {:<20}".format("CALL", "QTH", "QSL"))
    print("{:<20} {:<20} {:<20}".format("CQ", "Calling any station", "Send QSL"))
    print("{:<20} {:<20} {:<20}".format("QRZ", "Who is calling me?", "Send QSL"))
    print("{:<20} {:<20} {:<20}".format("QSO", "I can hear you", "QSL received"))
    print("{:<20} {:<20} {:<20}".format("73", "Goodbye", "Best regards"))
    print("\n")
    print(Fore.LIGHTBLUE_EX)    

def Radio(model, status):
    # Open the file in append mode
    with open("./data/Shack.txt", "a") as file:
        
        # Append a new line character to the end of the file
        file.write("\n")
        
        # Write the new line of text to the next free line
        file.write("[" + str(model) + "]\t Status: " + str(status   ))

def getRadios():
    print(Fore.LIGHTCYAN_EX)
    radios = open("./data/Shack.txt")

    print(radios.read())
    print("\n")
    print(Fore.LIGHTBLUE_EX)  