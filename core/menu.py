from core import util
from core import analyze
from core import report

def show_main_menu():

    while True:
        report.welcome()
        print("1. Analyze PC Health")
        print("2. About")
        print("3. Exit")
        util.space()

        choice = input("Select an option:")

        if choice == "1":
            util.space()
            analyze.analyze_pc()
            util.space()

        elif choice == "2":
            util.space()
            print("OberClock v0.3alpha")
            print("Created by Thomas Obermark")
            util.space()

        elif choice == "3":
            util.space()
            print("Thank you for using OberClock!")
            break

        else:
            util.space()
            print("❌ Invalid option. Please try again.")
            util.space()

        util.space()
        input("Press Enter to return to the menu...")