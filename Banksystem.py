class Bank:

  def __init__(self, name, number, passcode):
    self.__name = name 
    self.__number = number 
    self.__passcode = passcode
    self.__checkings = 100
    self.__savings = 100

#This prints the user's checkings balance.
  def ViewCheckingsBalance(self):
    print "\nHere is your checkings balance ${:,}".format(self.__checkings)
     
#This prints the user's savings balance.
  def ViewSavingsBalance(self):
    print "\nHere is your savings balance ${:,}".format(self.__savings)

#This allows the user do withdraw cash from the atm. If there is not enough, it will tell the user so.
  def WithdrawCash(self):
      amount1 = int(raw_input ("How much would you like to withdraw? "))
      if amount1 > self.__checkings:
        print "\nYou do not have that much money."
      else:
        self.__checkings = self.__checkings - amount1
        print "\nYour total checkings is now ${:,}".format(self.__checkings)

#This part of the program will allow the user to deposit any amount of money into the atm.
  def DepositCashIntoChecking(self):
      amount2 = int(raw_input ("How much would you like to deposit to your checkings? "))
      self.__checkings = self.__checkings + amount2
      print "\nYour total checkings is now ${:,}".format(self.__checkings)

#This part of the program allows for the user to transfer money to the other account. It will tell the user if there is not enough money to be transfered.
  def TransferFundsFromAccounts(self):
      print "\nWould you like to transfer from your checkings to savings (1) or from savings to checkings (2)"
      answer = raw_input("Your choice: ")
      if answer == "1":
        ask2 = int(raw_input("How much would you like to transfer from your checkings to your savings. "))
        if ask2 > self.__checkings:
          print "\nYou do not have that much in your checkings"
        else:
          self.__savings = self.__savings + ask2
          self.__checkings = self.__checkings - ask2
          print "\nTransaction completed"
      if answer == "2":
        ask2 = int(raw_input("How much would you like to transfer from your savings to your checkings."))
        if ask2 > self.__savings:
          print "\nYou do not have that much in your checkings you have" 
        else:
          self.__checkings = self.__checkings + ask2
          self.__savings = self.__savings - ask2  
          print "Transaction completed"

#This part will print the savings, checkings, account number and name but not the password because that sould not be displayed.
  def ViewSummaryofAccount(self):
      print "Here is your summary"
      print "Name: " + str(self.__name)
      print "Accout Number: " + str(self.__number)
      print "Checkings Balance: ${:,}".format(self.__checkings)  
      print "Savings Balance: ${:,}".format(self.__savings)

#This part of the program will end the session and ask if the user would like a recipt. If they do, it will print the summary in a separate txt file.

  def TerminateSession(self):
      print "Thank you for visiting Luke's Bank"
      ask4 = raw_input("Would you like a recipt? ")
      if ask4.lower() == "yes":
        doc = open("Recipt.txt", "w+")
        doc.write("Here is your recipt\n")
        doc.write("Name: " + str(self.__name))
        doc.write("\nAccout Number: " + str(self.__number))
        doc.write("\nCheckings Balance: ${:,}".format(self.__checkings))
        doc.write("\nSavings Balance ${:,}".format(self.__savings))
        print "Thank you your recipt has been printed."
      print "Come back again!"
      return False

  
#This part ask fot he user to enter their username ans password. The user gets 3 tries to enter their password. There are unlimited tried to enter the accout number.
  def Login(self):
    print "\nHello welcome to Luke's Bank"
    print "\nPlease enter your accout number and password."
    question = raw_input("Acount number: ")
    while question.lower() != self.__number:
      print "\nWe do not recignize this accout."
      question = raw_input("Account number: ")
    question = raw_input("Password: ")
    count2 = 0
    count = 0
    while question.lower() != self.__passcode and count2 < 3:
      print "\nIncorrect Password"
      count2 = count2 + 1
      question = raw_input("Password attempt "+ str(count2)+ " of 3: ")
      if count2 == 3:
        count = 1
        print "You are locked out of the atm."
    return True