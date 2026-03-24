data = []
count = 0
with open(r'C:\Users\yngwi\OneDrive\桌面\reviews_analytics\reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print(len(data))
print("--------------------")
print(data[0])
