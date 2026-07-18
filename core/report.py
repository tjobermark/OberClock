from core import hardware
from core import util

GREAT = 5
GOOD = 3
POOR = 1

GREAT_OVERALL_SCORE = 15
GOOD_OVERALL_SCORE = 10

MAX_SCORE = 15

def welcome():
    util.thick_divider()
    print("            OberClock")
    util.thick_divider()
    print("PC Health Analyzer")
    util.space()
    print("Version 3.0")
    util.space()

def print_gpu_names():
    gpu_names = hardware.get_gpu_names()
    if gpu_names:
        print(f"GPU: {', '.join(gpu_names)}")
    else:
        print("GPU: Not found")

def print_ram_info():
    ram_modules = hardware.get_ram_modules()
    if ram_modules:
        print("RAM:")
        for module in ram_modules:
            print(f"    - {module['manufacturer']} {module['part_number']} ({module['capacity']} GB @ {module['configured_speed_MHz']} MHz)")
    else:
        print("RAM: Not found")

def print_system_info():
    print("System Information:")
    util.thin_divider()
    util.space()
    print(f"CPU: {hardware.get_cpu_name()}")
    print_gpu_names()
    print_ram_info()
    print(f"XMP/EXPO enabled: {util.true_false_yes_no(hardware.is_xmp_expo_enabled())}")
    print(f"Motherboard: {hardware.get_board_name()}")
    print(f"BIOS version: {hardware.get_bios_version()}")
    print(f"Operating System: {hardware.get_os_name()}")
    print(f"Storage: ")
    for drive_name in hardware.get_storage_names():
        print(f"    - {drive_name}")

def print_ram_status_recommendations(ram_score, xmp_expo,):
    print("Recommendations for improving RAM Speed:")
    if ram_score == GREAT:
    
        if xmp_expo == True:
            print("1. No immediate action needed.")
        else:
            print("1. Enable XMP/EXPO for better performance.")

    elif ram_score == GOOD:
        
        if xmp_expo == True:
            print("1. No immediate action needed.")
        else:
            print("1. Enable XMP/EXPO for better performance.")
        
        print("2. Consider upgrading to more RAM.")
    else:
        print("1. Upgrade to more RAM immediately.")


def print_ram_status(ram_score,rec_answer,xmp_expo):
    print("RAM Status:")
    util.thin_divider()
    util.space()
    if ram_score == GREAT:
        print("✅ Plenty of RAM for modern games.")
        print(f"Score {ram_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
            print_ram_status_recommendations(ram_score, xmp_expo)
    elif ram_score == GOOD:
        print("⚠️ Good, but an upgrade may help.")
        print(f"Score {ram_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
            print_ram_status_recommendations(ram_score, xmp_expo)
    else:
        print("❌ Gaming performance may suffer.")
        print(f"Score {ram_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
            print_ram_status_recommendations(ram_score, xmp_expo)

def print_disk_status(disk_score, rec_answer):
    print("Disk Status:")
    util.thin_divider()
    util.space()
    if disk_score == GREAT:
        print("✅ Plenty of free disk space.")
        print(f"Score {disk_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
            print_disk_status_recommendations(disk_score)
    elif disk_score == GOOD:
        print("⚠️ Adequate free disk space, but consider cleaning up.")
        print(f"Score {disk_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
            print_disk_status_recommendations(disk_score)
    else:
        print("❌ Insufficient free disk space!")
        print(f"Score {disk_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
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
    util.thin_divider()
    util.space()
    if cpu_score == GREAT:
        print("✅ CPU temperature is within safe limits.")
        print(f"Score {cpu_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
            print_cpu_status_recommendations(cpu_score)
    elif cpu_score == GOOD:
        print("⚠️ CPU temperature is getting high.")
        print(f"Score {cpu_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
            print_cpu_status_recommendations(cpu_score)
    else:
        print("❌ CPU temperature is too high!")
        print(f"Score {cpu_score} / {GREAT}")
        if rec_answer == "yes":
            util.space()
            print_cpu_status_recommendations(cpu_score)


def print_overall_status(total_score, top_score):
    util.thin_divider()
    print("Overall Status:")
    util.thin_divider()
    util.space()
    print(f"Overall Health: {util.percentage(total_score, top_score):.0f}%")
    if total_score == GREAT_OVERALL_SCORE:
        print("✅ Your PC is in excellent health!")
    elif total_score >= GOOD_OVERALL_SCORE:
        print("⚠️ Your PC is in good health, but there's room for improvement.")
    else:
        print("❌ Your PC needs attention.")

def print_report(ram_score, cpu_score, disk_score, total_score, top_score, rec_answer, xmp_expo):
    util.thick_divider()
    print("    OberClock: PC Health Report")
    util.thick_divider()
    print("PC Health Report")
    util.space()
    print_ram_status(ram_score, rec_answer, xmp_expo)
    util.space()
    print_cpu_status(cpu_score, rec_answer)
    util.space()
    print_disk_status(disk_score, rec_answer)
    util.space()
    print_overall_status(total_score, top_score)