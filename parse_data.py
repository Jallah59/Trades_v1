import time

file_path = "live_data.csv"
graph_data = open('data.csv','r').read()
lines = graph_data.split('\n')
print("opened files")

for line in lines:
    with open(file_path, 'a') as file:
        print(line)
        file.write(line +"\n")
        time.sleep(0.1)
