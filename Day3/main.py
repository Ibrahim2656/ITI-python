"""



"""


from MathAutomation import math_report
from RegexLogCleaner import regex_log_cleaner
from DatetimeReminder import datetime_reminder
from ProductDataTransformer import product_data_transformer
from OSFileManager import os_file_manager
from RandomDataGenerator import random_data_generator
tasks={
   1:("Math Automation",math_report),
   2:("Regex Log Cleaner", regex_log_cleaner),
   3:("Datetime Reminder Script",datetime_reminder),
   4: ("Product Data Transformer", product_data_transformer),
   5: ("OS File Manager", os_file_manager),
   6: ("Random Data Generator", random_data_generator),
}


def show_menu():
   """Display menu of tasks."""
   print("\nAvailable Tasks:")
   for num, (name, _) in tasks.items():
      print(f"  {num}. {name}")


def get_choice():
   while True:
      try:
         choice=int(input("\n Enter the task number to run: "))
         if choice in tasks:
            return choice
         else:
            print("Invalid choice! Please enter a valid task number.")
      except ValueError:
         print("Invalid input! Please enter a number")
         
         
def main():
   show_menu()
   choice=get_choice()
   print(f"\n Running Task {choice}: {tasks[choice][0]}\n")
   task_function=tasks[choice][1]
   task_function()



if __name__ == '__main__':
   main()
   

