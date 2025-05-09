import ctypes

# Panggil fungsi LockWorkStation dari user32.dll
ctypes.windll.user32.LockWorkStation()
