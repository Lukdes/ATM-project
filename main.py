from Banksystem import Bank
Luke = Bank("Luke", "1234" , "4321" )
go = Luke.Login()

while go:


  #once acess is granted, you need to choose one of the seven choices and then hit enter. If something else is typed you are told to choose a number from 1 to 7


    print "__________________________________________________"
    print "1) View Checkings Balance"
    print "2) View Savings Balance"
    print "3) Withdraw Cash"
    print "4) Desposit Cash"
    print "5) Transfer Money"
    print "6) View Summary"
    print "7) End session"
    print "__________________________________________________"
    question = raw_input("What would you like to do? ")
    print "__________________________________________________"
    if question == "1":
      Luke.ViewCheckingsBalance()
    elif question == "2":
      Luke.ViewSavingsBalance()
    elif question == "3":
      Luke.WithdrawCash()
    elif question == "4":
      Luke.DepositCashIntoChecking()
    elif question == "5":
      Luke.TransferFundsFromAccounts()
    elif question == "6":
      Luke.ViewSummaryofAccount()
    elif question == "7":
      count = 1
      go = Luke.TerminateSession()
    else:
      print "Please choose a number from 1 to 7"