class moneyCreditWithdrawSystem:
    # Constructor for the moneyCreditWithdrawSystem class.
    def __init__(self):
        pass
    
    # Method to initialize the entrance process.
    def entrance_process_init(self):
        # Check if the retry limit has not been exceeded.
        if self.entrance_retry < 3:
            # Displaying the options for the user to choose from.
            print('''Please select your options from below:
                1. Enter 1 for Registration 
                2. Enter 2 for Login
                ''')
            # Taking user input for the entrance process.
            try:
                self.enter_process = int(input())
            # Handling the exceptions when the use give the wrong input.
            except Exception as e:
                # Increment the retry counter.
                self.entrance_retry += 1
                # Display an error message if the retry limit has not been reached.
                if self.entrance_retry != 3:
                     print(f"Please enter only numeric values. Your input {str(e).split()[-1]} is not valid")
                # Call the method again for a valid input.
                self.entrance_process_init()
                return False
                
            print(self.enter_process)
            
            # Navigate to Registration process if the user selects option 1.
            if self.enter_process == 1:
                print("Navigating to Registration")
            # Navigate to Login process if the user selects option 2.
            elif self.enter_process == 2:
                print("Navigating to Login")
            # If the user enters an invalid option, prompt them to choose again.
            else:
                 # Increment the retry counter.
                self.entrance_retry += 1
                # Display an error message if the retry limit has not been reached.
                print(f"{self.entrance_retry}")
                if self.entrance_retry != 3:
                    print("Please choose the correct entrance process number: 1 or 2")
                # Call the method again for a valid input.
                self.entrance_process_init()
        else:
            # If retry limit exceeded, inform the user and terminate the process.
            print("Entrance process retry exceeded over 3 times. Unfortunately, we can't process your request due to incorrect input.")

# Defining the main function.
# The project process starts from here.
if __name__ == '__main__':
    # Printing the welcome message to the user.
    print('Hi, Welcome to Money Credit Withdrawal System')
    print('I am assisting with credit and withdrawal from your bank account')
   
    # Creating an object for the moneyCreditWithdrawSystem class.
    main_object = moneyCreditWithdrawSystem()
    
    # Assigning an entrance_retry variable to control wrong information from the user during the entrance process.
    main_object.entrance_retry = 0
    # Calling the entrance process method.
    main_object.entrance_process_init()
