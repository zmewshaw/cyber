#Skytrain Inc Ticket Validation System 0.1
#Do not distribute this file.

def load_file(loc):
    if loc.endswith(".md"):
        return open(loc, 'r')
    else:
        print("Wrong file type.")
        exit()

def evaluate(ticketFile):
    #Evaluates a ticket to check for ireggularities.
    code_line = None
    for i,x in enumerate(ticketFile.readlines()):
        if i == 0:
            if not x.startswith("# Skytrain Inc"):
                print("Fail i=0")
                return False
            continue
        if i == 1:
            if not x.startswith("## Ticket to "):
                print("Fail i=1")
                return False
            print(f"Destination: {' '.join(x.strip().split(' ')[3:])}")
            continue

        if x.startswith("__Ticket Code:__"):
            code_line = i+1
            continue

        if code_line and i == code_line:
            if not x.startswith("**"):
                return False
            ticketCode = x.replace("**", "").split("+")[0]
            print(ticketCode)
            if int(ticketCode) % 7 == 4:
                validationNumber = eval(x.replace("**", ""))
                print("num: " + str(validationNumber))
                if validationNumber > 100:
                    return True
                else:
                    return False
    print("Fail end")
    return False

def main():
    fileName = "test.md"
    ticket = load_file(fileName)
    #DEBUG print(ticket)
    result = evaluate(ticket)
    if (result):
        print("Valid ticket.")
    else:
        print("Invalid ticket.")
    ticket.close

main()

