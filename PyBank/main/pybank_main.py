import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")
output_file = os.path.join("..", "analysis", "results.txt")

with open(output_file, "w") as file:    
    file.write("Financial Analysis\n")
    file.write("---------------------------------\n")

    # Declaring variables
    total_months = 0
    total_profit_loss = 0
    previous_profit_loss = 0
    profit_loss_changes = []
    dates = []   
    max_increase = 0
    max_decrease = 0
    max_increase_date = ""
    max_decrease_date = ""

    # Opening the csv and read it 
    with open(budget_data_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
    
        #code to removing the header
        csv_header = next(csv_reader)

     
        for row in csv_reader:
         
            total_months = total_months + 1  

            # get profit/loss from current row
            current_profit_loss = int(row[1])  
            dates.append(row[0])  

            #total profit/loss
            total_profit_loss += current_profit_loss

            # calculate change from previous month
            if total_months > 1:
                profit_loss_change = current_profit_loss - previous_profit_loss
                profit_loss_changes.append(profit_loss_change)

                # track greatest increase and decrease
                if profit_loss_change > max_increase:
                    max_increase = profit_loss_change
               
                    #code to get the increase date
                    max_increase_date = row[0]   

                if profit_loss_change < max_decrease:
                    max_decrease = profit_loss_change
                    max_decrease_date = row[0]  # Date corresponding to max decrease

            # Update previous profit/loss for the next iteration
            previous_profit_loss = current_profit_loss

    # Calculate the average change
    average_change = (round(sum(profit_loss_changes) / len(profit_loss_changes),2))

    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: $ {(round(average_change,2))}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")

print ("")
print("Financial Analysis")
print("")
print("___________________________")
print("")
print(f"Total Months: {total_months}")
print("")
print(f"Total: ${total_profit_loss}")
print("")
print(f"Average Change: ${(round(average_change,2))}")
print("")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print("")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")
print("")
print("Your file was successfully created!")
print("")
