# # # # # # # import os
# # # # # # # import shutil
# # # # # # # import string
# # # # # # # from pathlib import Path

# # # # # # # def find_and_move_xlsx(target_folder):
# # # # # # #     # Create target folder if not exists
# # # # # # #     os.makedirs(target_folder, exist_ok=True)

# # # # # # #     # Check available drives except C:
# # # # # # #     drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\") and d != "C"]
    
# # # # # # #     # Add Downloads folder manually
# # # # # # #     downloads_folder = str(Path.home() / "Downloads")
# # # # # # #     if os.path.exists(downloads_folder):
# # # # # # #         drives.append(downloads_folder)

# # # # # # #     print("Scanning:", drives)

# # # # # # #     for drive in drives:
# # # # # # #         for root, dirs, files in os.walk(drive, topdown=True, followlinks=False):
# # # # # # #             for file in files:
# # # # # # #                 if file.endswith(".xlsx"):
# # # # # # #                     source_path = os.path.join(root, file)
# # # # # # #                     dest_path = os.path.join(target_folder, file)

# # # # # # #                     # Agar same naam ki file already hai to rename kar dena
# # # # # # #                     if os.path.exists(dest_path):
# # # # # # #                         base, ext = os.path.splitext(file)
# # # # # # #                         counter = 1
# # # # # # #                         while os.path.exists(dest_path):
# # # # # # #                             dest_path = os.path.join(target_folder, f"{base}_{counter}{ext}")
# # # # # # #                             counter += 1
                    
# # # # # # #                     try:
# # # # # # #                         shutil.move(source_path, dest_path)
# # # # # # #                         print(f"Moved: {source_path} -> {dest_path}")
# # # # # # #                     except Exception as e:
# # # # # # #                         print(f"Error moving {source_path}: {e}")

# # # # # # # if __name__ == "__main__":
# # # # # # #     # Jahan saari files collect hongi (Desktop par ek naya folder banega)
# # # # # # #     target_folder = str(Path.home() / "Desktop" / "Collected_XLSX")
# # # # # # #     find_and_move_xlsx(target_folder)
# # # # # # #     print("✅ All .xlsx files moved successfully (D:, E:, F: + Downloads)!")

# # # # # # import os
# # # # # # import shutil
# # # # # # from pathlib import Path

# # # # # # def find_and_move_xlsx(target_folder):
# # # # # #     os.makedirs(target_folder, exist_ok=True)

# # # # # #     # Sirf Downloads + D/E drives check karna for safety
# # # # # #     search_paths = [
# # # # # #         str(Path.home() / "Downloads"),
# # # # # #         "D:\\",
# # # # # #         "E:\\"
# # # # # #     ]

# # # # # #     for drive in search_paths:
# # # # # #         if os.path.exists(drive):
# # # # # #             for root, dirs, files in os.walk(drive, topdown=True, followlinks=False):
# # # # # #                 for file in files:
# # # # # #                     if file.endswith(".xlsx"):
# # # # # #                         source_path = os.path.join(root, file)
# # # # # #                         dest_path = os.path.join(target_folder, file)

# # # # # #                         if os.path.exists(dest_path):
# # # # # #                             base, ext = os.path.splitext(file)
# # # # # #                             counter = 1
# # # # # #                             while os.path.exists(dest_path):
# # # # # #                                 dest_path = os.path.join(target_folder, f"{base}_{counter}{ext}")
# # # # # #                                 counter += 1
# # # # # #                         try:
# # # # # #                             shutil.move(source_path, dest_path)
# # # # # #                             print(f"Moved: {source_path} -> {dest_path}")
# # # # # #                         except Exception as e:
# # # # # #                             print(f"Error moving {source_path}: {e}")

# # # # # # if __name__ == "__main__":
# # # # # #     # Yahan aap apna OneDrive Desktop ka path dal do
# # # # # #     target_folder = str(Path.home() / "OneDrive" / "Sayed - Personal" / "Desktop" / "Collected_XLSX")
# # # # # #     find_and_move_xlsx(target_folder)
# # # # # #     print("✅ All .xlsx files moved successfully to OneDrive Desktop!")

# # # # # from pathlib import Path

# # # # # # Normal Desktop path (local)
# # # # # local_desktop = Path.home() / "Desktop"

# # # # # # OneDrive Desktop path (sync wala)
# # # # # onedrive_desktop = Path.home() / "OneDrive" / "Sayed - Personal" / "Desktop"

# # # # # print("Local Desktop path:", local_desktop)
# # # # # print("OneDrive Desktop path:", onedrive_desktop)

# # # # # # Check agar Collected_XLSX bana hai to uska path show karo
# # # # # local_folder = local_desktop / "Collected_XLSX"
# # # # # onedrive_folder = onedrive_desktop / "Collected_XLSX"

# # # # # if local_folder.exists():
# # # # #     print("✅ Collected_XLSX found in Local Desktop:", local_folder)
# # # # # elif onedrive_folder.exists():
# # # # #     print("✅ Collected_XLSX found in OneDrive Desktop:", onedrive_folder)
# # # # # else:
# # # # #     print("❌ Collected_XLSX folder not found yet.")

# # # # import os
# # # # import shutil
# # # # from pathlib import Path

# # # # # Jahan folder banana hai (OneDrive Desktop)
# # # # desktop = Path.home() / "OneDrive" / "Sayed - Personal" / "Desktop"
# # # # target_folder = desktop / "Collected_XLSX"
# # # # target_folder.mkdir(exist_ok=True)

# # # # # Common folders jahan xlsx files hoti hain
# # # # folders_to_scan = [
# # # #     Path.home() / "Downloads",
# # # #     Path.home() / "Documents",
# # # #     Path.home() / "Desktop",
# # # #     Path.home() / "OneDrive" / "Sayed - Personal" / "Desktop",
# # # # ]

# # # # # Scan and move
# # # # for folder in folders_to_scan:
# # # #     if folder.exists():
# # # #         for root, _, files in os.walk(folder):
# # # #             for file in files:
# # # #                 if file.endswith(".xlsx"):
# # # #                     source = Path(root) / file
# # # #                     destination = target_folder / file
# # # #                     # Agar duplicate file ho to overwrite karne ke liye
# # # #                     if destination.exists():
# # # #                         destination.unlink()
# # # #                     shutil.move(str(source), str(destination))
# # # #                     print(f"Moved: {source} -> {destination}")

# # # # print(f"\n✅ All .xlsx files moved to: {target_folder}")


# # # import os
# # # import shutil
# # # from pathlib import Path

# # # # Jahan folder banana hai (OneDrive Desktop)
# # # desktop = Path.home() / "OneDrive" / "Sayed - Personal" / "Desktop"
# # # target_folder = desktop / "Collected_XLSX"
# # # target_folder.mkdir(exist_ok=True)

# # # # Common folders jahan xlsx files hoti hain
# # # folders_to_scan = [
# # #     Path.home() / "Downloads",
# # #     Path.home() / "Documents",
# # #     Path.home() / "Desktop",
# # #     Path.home() / "OneDrive" / "Sayed - Personal" / "Desktop",
# # # ]

# # # # Scan and move
# # # for folder in folders_to_scan:
# # #     if folder.exists():
# # #         for root, _, files in os.walk(folder):
# # #             for file in files:
# # #                 if file.endswith(".xlsx"):
# # #                     source = Path(root) / file
# # #                     destination = target_folder / file

# # #                     # Skip agar already Collected_XLSX me hi ho
# # #                     if source.parent == target_folder:
# # #                         continue  

# # #                     # Agar duplicate file hai to overwrite
# # #                     if destination.exists():
# # #                         destination.unlink()

# # #                     shutil.move(str(source), str(destination))
# # #                     print(f"Moved: {source} -> {destination}")

# # # print(f"\n✅ All .xlsx files moved to: {target_folder}")

# # import os
# # import shutil

# # # Apna Desktop ka path yahan dalna
# # desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# # # New folder ka naam
# # new_folder = os.path.join(desktop_path, "SQL_Files")

# # # Agar folder exist nahi karta to create karo
# # if not os.path.exists(new_folder):
# #     os.makedirs(new_folder)

# # # Current directory jahan SQL files hain
# # current_dir = os.getcwd()

# # # Har file ko check karo
# # for file in os.listdir(current_dir):
# #     if file.endswith(".sql"):
# #         source = os.path.join(current_dir, file)
# #         destination = os.path.join(new_folder, file)
# #         shutil.move(source, destination)
# #         print(f"Moved: {file}")

# # print("✅ All SQL files moved to Desktop/SQL_Files")

# import os
# import shutil

# # Desktop ka path
# desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# # SQL files ke liye naya folder
# sql_folder = os.path.join(desktop_path, "Collected_SQL")
# os.makedirs(sql_folder, exist_ok=True)

# # Puri system drive scan karni ho (jaise Excel ke liye kiya tha)
# drives = ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\"]  # apne PC ki drives ke hisaab se update karna

# for drive in drives:
#     for root, dirs, files in os.walk(drive):
#         for file in files:
#             if file.lower().endswith(".sql"):
#                 try:
#                     source = os.path.join(root, file)
#                     destination = os.path.join(sql_folder, file)

#                     # agar same naam ki file already hai to rename karke save karega
#                     if os.path.exists(destination):
#                         base, ext = os.path.splitext(file)
#                         count = 1
#                         while os.path.exists(destination):
#                             destination = os.path.join(sql_folder, f"{base}_{count}{ext}")
#                             count += 1

#                     shutil.move(source, destination)
#                     print(f"Moved: {source} -> {destination}")

#                 except Exception as e:
#                     print(f"❌ Error moving {file}: {e}")

# print("✅ Saari .SQL files Desktop ke 'Collected_SQL' folder me move ho gayi.")


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


LOGIN_URL = "http://127.0.0.1:5000/"
USERNAME = "demo_user"
PASSWORD = "demo_pass"
MESSAGE = "Sorry"
COUNT = 25
DELAY = 0.2 # seconds between sends


# Launch Chrome (auto-manages ChromeDriver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def wait_and_type(by, selector, text):
	elem = None
	# naive wait loop
	for _ in range(50):
		try:
			elem = driver.find_element(by, selector)
			break
		except Exception:
			time.sleep(0.1)
	if not elem:
		raise RuntimeError(f"Element not found: {selector}")
	elem.clear()
	elem.send_keys(text)


try:
	# 1) Open login page
	driver.get(LOGIN_URL)

	# 2) Fill creds & login
	wait_and_type(By.ID, "username", USERNAME)
	wait_and_type(By.ID, "password", PASSWORD)
	driver.find_element(By.ID, "login-btn").click()

	# 3) On chat page, send messages repeatedly
	for i in range(COUNT):
		wait_and_type(By.ID, "message", f"{MESSAGE} #{i+1}")
		driver.find_element(By.ID, "send-btn").click()
		time.sleep(DELAY)

	time.sleep(2) # keep window open briefly to view results
finally:
	driver.quit()