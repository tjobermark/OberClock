from core import util
from core import report
from core import hardware

GREAT_RAM_AMOUNT = 31  # in GB
GOOD_RAM_AMOUNT = 15  # in GB

GREAT_DISK_SPACE = 250  # in GB
GOOD_DISK_SPACE = 100   # in GB

GREAT_CPU_TEMP = 70  # in Celsius
GOOD_CPU_TEMP = 80   # in Celsius

GREAT_OVERALL_SCORE = 15
GOOD_OVERALL_SCORE = 10

MAX_SCORE = 15

def check_ram(ram_size, great_amount, good_amount):
    return util.rate_high_good(ram_size, great_amount, good_amount)

def check_disk(free_space, great_amount, good_amount):
    return util.rate_high_good(free_space, great_amount, good_amount)

def check_cpu(cpu_temp, great_temp, good_temp):
    return util.rate_low_good(cpu_temp, great_temp, good_temp)

def analyze_pc():

    ram = hardware.get_total_ram()

    free_space = hardware.get_free_disk_space()

    cpu_temp = int(input("Please enter your CPU Temperature (°C): "))

    rec_answer = util.ask_yes_no("Do you want recommendations for improving your PC's health? (yes/no): ")

    cpu_score = check_cpu(cpu_temp, GREAT_CPU_TEMP, GOOD_CPU_TEMP)

    ram_score = check_ram(ram, GREAT_RAM_AMOUNT, GOOD_RAM_AMOUNT)

    disk_score = check_disk(free_space, GREAT_DISK_SPACE, GOOD_DISK_SPACE)

    total_score = ram_score + cpu_score + disk_score

    top_score = MAX_SCORE

    xmp_expo = hardware.is_xmp_expo_enabled()
 
    report.print_report(ram_score, cpu_score, disk_score, total_score, top_score, rec_answer, xmp_expo)

