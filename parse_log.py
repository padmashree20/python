# Open the log file
file = open("access.log", "r")

for line in file:
    parts = line.split()

    ip = parts[0]
    date = parts[3]
    method = parts[5].replace('"','')
    page = parts[6]
    status = parts[8]

    print("IP Address:", ip)
    print("Date:", date)
    print("Method:", method)
    print("Page:", page)
    print("Status Code:", status)
    print("-------------------")

file.close()