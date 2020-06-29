total_over= 50
current_over= int(input("Enter curent over: "))
made_run= int(input("Enter run made by opponent: "))
current_run= int(input("Enter current run: "))
remaining_run= made_run - current_run
remaining_over= total_over- current_over 
print("Current run rate: ", current_run/current_over)
print("Required run rate: ", remaining_run/remaining_over)