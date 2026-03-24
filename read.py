data = []
count = 0
with open(r'C:\Users\yngwi\OneDrive\桌面\reviews_analytics\reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print("檔案讀取完,總共有",len(data),"筆資料")

sum_len = 0
for line2 in data:
    sum_len += len(line2)
print("平均長度",sum_len / len(data))
    

