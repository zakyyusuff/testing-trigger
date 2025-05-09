# import subprocess

# # Path untuk AutoHotkey dan skrip AHK
# ahk_script = r"C:\scripts\rtr-ahk1.ahk"
# ahk_executable = r"C:\Program Files\AutoHotkey\v2\AutoHotkey.exe"  # Path executable AutoHotkey

# # Menangani tanda kutip untuk PowerShell
# cmd_command = f"& '{ahk_executable}' '{ahk_script}'"

# # Membuka PowerShell dan menjalankan perintah
# subprocess.Popen(['powershell', '-Command', cmd_command])

# print("PowerShell telah dibuka dan perintah dijalankan.")




# # /////////////////////////////// 2
# import subprocess
# import time

# print("Opening PowerShell...")
# try:
#     subprocess.run(["powershell", "-Command", "Start-Process cmd -ArgumentList '/c echo Hello from CMD'"])
#     print("PowerShell opened successfully.")
# except Exception as e:
#     print(f"Error: {e}")




# ////////////////////////////////////// 3
import subprocess

# Path untuk AutoHotkey dan skrip AHK
ahk_script = r"C:\scripts\rtr-ahk1.ahk"
ahk_executable = r"C:\Program Files\AutoHotkey\v2\AutoHotkey.exe"  # Path executable AutoHotkey

# Menangani tanda kutip untuk PowerShell
cmd_command = f"& '{ahk_executable}' '{ahk_script}'"

# Membuka PowerShell dan menjalankan perintah dengan menggunakan subprocess
try:
    subprocess.run(["powershell", "-NoExit", "-Command", cmd_command], check=True)
    print("PowerShell telah dibuka dan perintah dijalankan.")
except subprocess.CalledProcessError as e:
    print(f"Terjadi error saat menjalankan PowerShell: {e}")

# Skrip lain untuk membuka cmd melalui PowerShell
try:
    print("Opening PowerShell for CMD...")
    subprocess.run(["powershell", "-NoExit", "-Command", "Start-Process cmd -ArgumentList '/c echo Hello from CMD'"], check=True)
    print("PowerShell membuka CMD berhasil.")
except subprocess.CalledProcessError as e:
    print(f"Terjadi error saat membuka CMD: {e}")
