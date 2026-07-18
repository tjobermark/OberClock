import psutil

GREAT_RAM_AMOUNT = 31  # in GB
GOOD_RAM_AMOUNT = 15  # in GB

GREAT_DISK_SPACE = 250  # in GB
GOOD_DISK_SPACE = 100   # in GB

GREAT_CPU_TEMP = 70  # in Celsius
GOOD_CPU_TEMP = 80   # in Celsius

GREAT = 5
GOOD = 3
POOR = 1

GREAT_OVERALL_SCORE = 15
GOOD_OVERALL_SCORE = 10

MAX_SCORE = 15

def thick_divider():
    print("===================================")

def thin_divider():
    print("-----------------------------------")

def space(lines=1):
    for _ in range(lines):
        print()

def percentage(value, total):
    return (value / total) * 100

def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        
        if answer in ["yes", "no"]:
            return answer
        
        print("Please enter 'yes' or 'no'.")

def rate_high_good(item, high_score, medium_score):
    if item >= high_score:
        return GREAT
    elif item >= medium_score:
        return GOOD
    else:
        return POOR
    
def rate_low_good(item, low_score, medium_score):
    if item <= low_score:
        return GREAT
    elif item <= medium_score:
        return GOOD
    else:
        return POOR

def welcome():
    thick_divider()
    print("            OberClock")
    thick_divider()
    print("PC Health Analyzer")
    space()
    print("Version 3.0")
    space()

def check_ram(ram_size):
    return rate_high_good(ram_size, GREAT_RAM_AMOUNT, GOOD_RAM_AMOUNT)

def check_disk(free_space):
    return rate_high_good(free_space, GREAT_DISK_SPACE, GOOD_DISK_SPACE)

def check_cpu(cpu_temp):
    return rate_low_good(cpu_temp, GREAT_CPU_TEMP, GOOD_CPU_TEMP)

def print_ram_status_recommendations(ram_score, xmp_expo):
    print("Recommendations for improving RAM Speed:")
    if ram_score == GREAT:
    
        if xmp_expo == "yes":
            print("1. No immediate action needed.")
        else:
            print("1. Enable XMP/EXPO for better performance.")

    elif ram_score == GOOD:
        
        if xmp_expo == "yes":
            print("1. No immediate action needed.")
        else:
            print("1. Enable XMP/EXPO for better performance.")
        
        print("2. Consider upgrading to more RAM.")
    else:
        print("1. Upgrade to more RAM immediately.")


def print_ram_status(ram_score,rec_answer,xmp_expo):
    print("RAM Status:")
    thin_divider()
    space()
    if ram_score == GREAT:
        print("✅ Plenty of RAM for modern games.")
        print(f"Score {ram_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_ram_status_recommendations(ram_score, xmp_expo)
    elif ram_score == GOOD:
        print("⚠️ Good, but an upgrade may help.")
        print(f"Score {ram_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_ram_status_recommendations(ram_score, xmp_expo)
    else:
        print("❌ Gaming performance may suffer.")
        print(f"Score {ram_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_ram_status_recommendations(ram_score, xmp_expo)

def print_disk_status(disk_score, rec_answer):
    print("Disk Status:")
    thin_divider()
    space()
    if disk_score == GREAT:
        print("✅ Plenty of free disk space.")
        print(f"Score {disk_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_disk_status_recommendations(disk_score)
    elif disk_score == GOOD:
        print("⚠️ Adequate free disk space, but consider cleaning up.")
        print(f"Score {disk_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_disk_status_recommendations(disk_score)
    else:
        print("❌ Insufficient free disk space!")
        print(f"Score {disk_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_disk_status_recommendations(disk_score)

def print_disk_status_recommendations(disk_score):
    print("Recommendations for improving disk health:")
    if disk_score == GREAT:
        print("1. No immediate action needed.")
    elif disk_score == GOOD:
        print("1. Consider cleaning up unnecessary files.")
        print("2. Run Windows Storage Sense regularly.")
    else:
        print("1. Delete unnecessary files and programs.")
        print("2. Consider upgrading to a larger storage device.")

def print_cpu_status_recommendations(cpu_score):
    print("Recommendations for improving CPU health:")
    if cpu_score == GREAT:
        print("1. No immediate action needed.")
    elif cpu_score == GOOD:
        print("1. Ensure proper ventilation and cooling.")
        print("2. Consider upgrading to a more efficient CPU cooler.")
        print("3. Try reapplying thermal paste.")
        print("4. Clean your PC's dust buildup.")
    else:
        print("1. Take immediate action to cool down your CPU.")
        print("2. Consider upgrading to a more efficient CPU cooler.")
        print("3. Try reapplying thermal paste.")
        print("4. Clean your PC's dust buildup.")


def print_cpu_status(cpu_score, rec_answer):
    print("CPU Status:")
    thin_divider()
    space()
    if cpu_score == GREAT:
        print("✅ CPU temperature is within safe limits.")
        print(f"Score {cpu_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_cpu_status_recommendations(cpu_score)
    elif cpu_score == GOOD:
        print("⚠️ CPU temperature is getting high.")
        print(f"Score {cpu_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_cpu_status_recommendations(cpu_score)
    else:
        print("❌ CPU temperature is too high!")
        print(f"Score {cpu_score} / {GREAT}")
        if rec_answer == "yes":
            space()
            print_cpu_status_recommendations(cpu_score)


def print_overall_status(total_score, top_score):
    thin_divider()
    print("Overall Status:")
    thin_divider()
    space()
    print(f"Overall Health: {percentage(total_score, top_score):.0f}%")
    if total_score == GREAT_OVERALL_SCORE:
        print("✅ Your PC is in excellent health!")
    elif total_score >= GOOD_OVERALL_SCORE:
        print("⚠️ Your PC is in good health, but there's room for improvement.")
    else:
        print("❌ Your PC needs attention.")

def print_report(ram_score, cpu_score, disk_score, total_score, top_score, rec_answer, xmp_expo):
    thick_divider()
    print("    OberClock: PC Health Report")
    thick_divider()
    print("PC Health Report")
    space()
    print_ram_status(ram_score, rec_answer, xmp_expo)
    space()
    print_cpu_status(cpu_score, rec_answer)
    space()
    print_disk_status(disk_score, rec_answer)
    space()
    print_overall_status(total_score, top_score)
    

def analyze_pc():

    ram = round(psutil.virtual_memory().total / (1024**3))

    disk = psutil.disk_usage("/")

    free_space = round(disk.free / (1024**3))

    cpu_temp = int(input("Please enter your CPU Temperature (°C): "))

    rec_answer = ask_yes_no("Do you want recommendations for improving your PC's health? (yes/no): ")

    cpu_score = check_cpu(cpu_temp)

    ram_score = check_ram(ram)

    disk_score = check_disk(free_space)

    total_score = ram_score + cpu_score + disk_score

    top_score = MAX_SCORE

    xmp_expo = ask_yes_no("Do you have XMP/EXPO enabled? (yes/no): ")
 
    print_report(ram_score, cpu_score, disk_score, total_score, top_score, rec_answer, xmp_expo)

def show_menu():

    while True:
        welcome()
        print ("1. Analyze PC Health")
        print ("2. About")
        print ("3. Exit")
        space()

        choice = input("Select an option:")

        if choice == "1":
            space()
            analyze_pc()
            space()

        elif choice == "2":
            space()
            print("OberClock v0.3alpha")
            print("Created by Thomas Obermark")
            space()

        elif choice == "3":
            space()
            print("Thank you for using OberClock!")
            break

        else:
            space()
            print("❌ Invalid option. Please try again.")
            space()

        space()
        input("Press Enter to return to the menu...")

show_menu()