class moneyCreditWithdrawSystem:
    #  pass
    def __init__(self) -> None:
        pass
    
    def entrance_process_init(self):
        if self.entrance_retry <= 3:
            print('''Please select the your options from below
                1. Enter 1 for Registration 
                2. Enter 2 for Login
                ''')
            self.enter_process=int(input())
            print(self.enter_process)
            if self.enter_process == 1:
                print(f"navigate to Registration")
            elif self.enter_process == 2:
                print(f"navigating to login")
            else:
                print(f"please choose the right entrance process nuyumber as 1 or 2")
                self.entrance_process_init()
               
        else:
            print(f"Entrance process retry exceeded over 3 times. unfortunatly we can't process your request due to incorrect input")

        
if __name__ == '__main__':
    print('Hi, Welocme to Money Credit Withdrawl System')
    print('I am assesting for credit and withdraw money from your bank account')
   
    main_object=moneyCreditWithdrawSystem()
    main_object.entrance_retry=0
    main_object.entrance_process_init()
    
