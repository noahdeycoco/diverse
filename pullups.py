#! usr/bin python 2.7
#-*- coding: utf-8 -*-

from datetime import timedelta, datetime
import time


def welcome():
    print("""   
                 ,#####,
                 #_   _#
                 |o` `O|
                 |  u  |
                 \  =  /
                 |\___/|
        ___ ____/:     :\____ ___
      .'   `.-===-\   /-===-.`   '.
     /      .-'''''-.-'''''-.      \  
    /'             =:=             '\ 
  .'  ' .:    o   -=:=-   o    :. '  `.
  (.'   /'. '-.....-'-.....-' .'\   '.)
  /' ._/   '''''.     --:--   .  \_. '\ 
 |  .'|      '''''.  ---:---     ''     |'.
 |  : |       |  ---:---  |       | :  |
  \ : |       |_____._____|       | : /
  /   (       |----|------|       )   \ 
 /... .|      |    |      |      |. ...\ 
|::::/''     /     |       \     ''\::::|
'''''       /'    .L_      `\      ''''
           /'-.,__/` `\__..-'\ 
          ;      /     \      ;
          :     /       \     |
          |    /         \.   |
          |`../           |  ,/
          ( _ )           |  _)
          |   |           |   |
          |___|           \___|
          :===|            |==|
           \  /            |__|
           /\/\           /'''''`8.__
           |oo|           \__.//___)
           |==|
           \__/
""")
    print("=== PULL UPS CALCULATOR ===")


def main():
    #Define time to reach goal
    start_date= datetime.now()
    end_date= start_date

    #User input verification
    def int_checker(int_checker_name, data_name):
        int_checker_checker = 0
        while int_checker_checker < 1:
            try:
                int_checker_name = int(int_checker_name)
            except ValueError:
                print(
                         "%s is not considered as a number. Please provide a right "
                         "integer.") % int_checker_name
                int_checker_name = input("How many " + data_name + " do you "
                                                                "want to do ? \n")
            else:
                if int_checker_name < 0:
                    print(
                        "How can you do negative %s ? Do you have the power to go "
                        "back in time as well?") % data_name
                    int_checker_name = input("How many" + data_name +" do "
                                                              "you want to do ? \n")
                if int_checker_name >= 0:
                    int_checker_checker += 1
                    return int(int_checker_name)


    #User input: repetitions, series and interruptions

    input_pullups_reps = input("How many pull ups can you do for one "
                                   "repetition?")
    input_pullups_reps = int_checker(input_pullups_reps, "repetitions")

    input_pullups_series= input("How many pull ups series do you do ?")
    input_pullups_series = int_checker(input_pullups_series, "series")

    input_nb_training_week = input("How many training by week have you plan?")
    input_nb_training_week = int_checker(input_nb_training_week, "training")

    total_pullups_week = int(input_pullups_reps)*int(input_pullups_series)*int(
        input_nb_training_week)

    input_pullups= input("How many pull ups do you want to do?")
    input_pullups = int_checker(input_pullups, "pull ups")

    interruption_week_choice = input(
        "\nDo you plan to have interruptions weeks ? ["
        "y/n]").lower()

    while interruption_week_choice not in ['y', 'n']:
        interruption_week_choice = input("\nPlease provide a right "
                                             "answer. \nDo you plan to have "
                                             "interruptions weeks ? ["
                        "y/n]").lower()


    start_time = time.time()

    interruption_week_choice_check = 0
    while interruption_week_choice_check < 1:
        try:
            string = str(interruption_week_choice)
        except ValueError:
            print("%s is not a correct answer.") % interruption_week_choice
            print(interruption_week_choice)
        else:
            if interruption_week_choice == 'n':
                print("No break? What a badass !")
                input_week_interruption = 0
                interruption_week_choice_check+=1
            if interruption_week_choice == 'y':
                input_week_interruption = input("How many interruption week "
                                                    "do you planned ?")
                input_week_interruption = int_checker(input_week_interruption,
                                                    "week interruption")
                interruption_week_choice_check += 1


    """
    total_pullups_training = input_pullups_reps*input_pullups_series
    
    print("To recap, for each training session, you'll do:\n - %s repetitions.\n "
          "- %s series.\n - %s in total.") %input_pullups_reps, input_pullups_series, total_pullups_training
    """


    week_number = 0
    pullups_counter = int(-input_week_interruption)*int(total_pullups_week)
    print(pullups_counter)
    print(input_pullups)
    print(total_pullups_week)

    while pullups_counter < input_pullups:
        week_number+=1
        pullups_counter+=total_pullups_week
        #print("At the end of week "+ str(week_number)+ ", you did :" +
              #str(pullups_counter))


    end_date = start_date + timedelta(weeks=week_number)
    print("\nIf you start right now, you'll be done on " + str(end_date.date()) + " after "+str(week_number)+" week(s) of "
          "training "
          "!")


    # restart programme
    #Join = input('Would you like to join me?').lower()
    #if Join.startswith('y'):

    print("\n--- Executed in %s seconds ---\n" % (time.time()
                                                                -start_time))

    response = input("\nDo you want to restart the programme? ["
                         "y/n]").lower()

    waiting_user_response = 0
    while waiting_user_response < 1:
        if response is None or response not in ['Y', 'y', 'N', 'n']:
            response =input("Please enter a valid option choice "
                             "[y/n]").lower()
        if response in ['y', 'yes']:
            main()
        else:
            waiting_user_response+=1
            print('Programm exit.')
            exit()

if __name__ == "__main__":
    welcome()
    main()
