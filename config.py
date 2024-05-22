import json

print("Reading and modifying config1.json...")
with open('C:/Users/Q1/PythonAlgoritmika/Ders3/config.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print("Modifying the data...")
data['author'] = 'Ali'
data['server']['port'] = 2024
data['server']['port2'] = 2025
data['openInBrowser'] = True
data['dist']['fonts'] = 'Arial, Helvetica, sans-serif'  

print("Writing the modified data to my_config.json...")
with open("my_config.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=2)

print("Configuration updated successfully.")
