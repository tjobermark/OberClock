ram_size = int(input("Enter your RAM size in GB: "))
print("Please close any unnecessary applications before proceeding.")
cpu_temp = int(input("Enter your CPU temperature in Celsius: "))
free_space = int(input("Enter your free disk space in GB: "))
score = 0

print("===================================")
print("      Gaming PC Health Report")
print("===================================")    
print()
print(f"CPU: Temperature = {cpu_temp}°C")



if cpu_temp >= 85:
    print("❌ CPU temperature is too high!")
    print("⭐")
    score += 1
elif cpu_temp >= 70:
    print("⚠️ CPU temperature is elevated.")
    print("⭐⭐⭐")
    score += 3
else:
    print("✅ CPU temperature is within normal range.")
    print("⭐⭐⭐⭐⭐")
    score += 5
print()
print(f"RAM: Size = {ram_size} GB")



if ram_size >= 32:
    print("✅ Plenty of RAM for modern games.")
    print("⭐⭐⭐⭐⭐")
    score += 5
elif ram_size >= 16:
    print("⚠️ Good, but an upgrade may help.")
    print("⭐⭐⭐")
    score += 3
else:
    print("❌ Gaming performance may suffer.")
    print("⭐")
    score += 1
print()
print(f"Free storage space = {free_space} GB")



if free_space >= 256:
    print("✅ Ample free disk space.")
    print("⭐⭐⭐⭐⭐")
    score += 5
elif free_space >= 128:
    print("⚠️ Adequate, but consider freeing up space.")
    print("⭐⭐⭐")
    score += 3
else:
    print("❌ Insufficient free disk space.")
    print("⭐")
    score += 1



print()
print(f"Total Health Score: {score}/15")



if score >= 12:
    print("🟢 Your PC is in excellent health!")
elif score >= 9:
    print("🟡 Your PC is in good health.")
else:
    print("🔴 Your PC needs some attention.")



print()
print("Recommendations:")



if cpu_temp >= 85:
    print("1: Implement better cooling solutions for your CPU. Examples include adding more fans, reapplying thermal paste, or upgrading your CPU cooler.")
elif cpu_temp >= 70:
    print("1: Consider cleaning your PC to improve airflow or reapplying thermal paste.")
else:
    print("1: No immediate action needed for CPU temperature.")

print()

if ram_size >= 32:
    print("2: No immediate action needed for RAM size.")
elif ram_size >= 16:
    print("2: Adding more RAM could improve performance in memory-intensive games.")
else:
    print("2: Adding more RAM is highly recommended to improve gaming performance. Especially if you are running modern games or multitasking while gaming.")

print()

if free_space >= 256:
    print("3: No immediate action needed for storage space.")
elif free_space >= 128:
    print("3: Consider freeing up disk space by uninstalling unused applications or moving files to an external drive.")
else:
    print("3: Freeing up disk space is highly recommended. Consider uninstalling unused applications, moving files to an external drive, or upgrading your storage solution.")