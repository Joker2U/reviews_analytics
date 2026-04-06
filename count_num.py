data = []
with open(r"C:\Users\yngwi\OneDrive\桌面\reviews_analytics\reviews.txt", "r") as f:
    for line in f:
        data.append(line)

wc ={}
for d in data:
    words = d.split()
    for word in words :
        if word in wc:
            wc[word] += 1 #有出現在字典裡就加一
        else:
            wc[word] = 1  #沒有出現就等於1
for word in wc:
    if wc[word] > 1000000: #假設出現超過10次
        print(word, wc[word])

# print(len(wc))  #印出這些字的總數量
# print(wc["Allen"])

while True:
    word = input("請問你想查甚麼字:")
    if word == 'q':
        break
    if word in wc:
        print(word,"出現過的次數為" , wc[word])
    else:
        print("沒有這個字")
print("退出")