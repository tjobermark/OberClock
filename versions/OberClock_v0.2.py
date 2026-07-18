def welcome():
    print("===================================")
    print("            OberClock")
    print("===================================")
    print("PC Health Analyzer")
    print()
    print("Version 2.0")


def check_ram(ram_size):
    if ram_size >= 32:
        return 5
    elif ram_size >= 16:
        return 3
    else:
        return 1


def check_cpu(cpu_temp):
    if cpu_temp <= 70:
        return 5
    elif cpu_temp <= 80:
        return 3
    else:
        return 1


def print_ram_status_recommendations(ram_score, xmp_expo):
    print("Recommendations for improving RAM health:")
    if ram_score == 5:
    
        if xmp_expo == "yes":
            print("1. No immediate action needed.")
        else:
            print("1. Enable XMP/EXPO for better performance.")

    elif ram_score == 3:
        
        if xmp_expo == "yes":
            print("1. No immediate action needed.")
        else:
            print("1. Enable XMP/EXPO for better performance.")
        
        print("2. Consider upgrading to more RAM.")
    else:
        print("1. Upgrade to more RAM immediately.")


def print_ram_status(ram_score,rec_answer,xmp_expo):
    print("RAM Status:")
    print("-----------------------------------")
    print()
    if ram_score == 5:
        print("✅ Plenty of RAM for modern games.")
        print("Score 5 / 5")
        if rec_answer == "yes":
            print()
            print_ram_status_recommendations(ram_score, xmp_expo)
    elif ram_score == 3:
        print("⚠️ Good, but an upgrade may help.")
        print("Score 3 / 5")
        if rec_answer == "yes":
            print()
            print_ram_status_recommendations(ram_score, xmp_expo)
    else:
        print("❌ Gaming performance may suffer.")
        print("Score 1 / 5")
        if rec_answer == "yes":
            print()
            print_ram_status_recommendations(ram_score, xmp_expo)


def print_cpu_status_recommendations(cpu_score):
    print("Recommendations for improving CPU health:")
    if cpu_score == 5:
        print("1. No immediate action needed.")
    elif cpu_score == 3:
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
    print("-----------------------------------")
    print()
    if cpu_score == 5:
        print("✅ CPU temperature is within safe limits.")
        print("Score 5 / 5")
        if rec_answer == "yes":
            print()
            print_cpu_status_recommendations(cpu_score)
    elif cpu_score == 3:
        print("⚠️ CPU temperature is getting high.")
        print("Score 3 / 5")
        if rec_answer == "yes":
            print()
            print_cpu_status_recommendations(cpu_score)
    else:
        print("❌ CPU temperature is too high!")
        print("Score 1 / 5")
        if rec_answer == "yes":
            print()
            print_cpu_status_recommendations(cpu_score)


def print_overall_status(total_score, top_score):
    print("-----------------------------------")
    print("Overall Status:")
    print("-----------------------------------")
    print()
    print(f"Overall Health: {total_score/top_score*100:.0f}%")
    if total_score == 10:
        print("✅ Your PC is in excellent health!")
    elif total_score >= 6:
        print("⚠️ Your PC is in good health, but there's room for improvement.")
    else:
        print("❌ Your PC needs attention.")

def print_report(ram_score, cpu_score, total_score, top_score, rec_answer, xmp_expo):
    print("===================================")
    print("    OberClock: PC Health Report")
    print("===================================")
    print("PC Health Report")
    print()
    print_ram_status(ram_score, rec_answer, xmp_expo)
    print()
    print_cpu_status(cpu_score, rec_answer)
    print()
    print_overall_status(total_score, top_score)

ram = int(input("Please enter the amount of RAM (GB) you have: "))

cpu_temp = int(input("Please enter your CPU Temperature (°C): "))

rec_answer = input("Do you want recommendations for improving your PC's health? (yes/no): ").lower()

cpu_score = check_cpu(cpu_temp)

ram_score = check_ram(ram)

total_score = ram_score + cpu_score

top_score = 10

xmp_expo = input("Do you have XMP/EXPO enabled? (yes/no): ").lower()

welcome()
print_report(ram_score, cpu_score, total_score, top_score, rec_answer, xmp_expo)