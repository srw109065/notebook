#讀取中文檔案 需加encoding = "utf-8"
with open("name.txt", "a", encoding = "utf-8") as n:
	while True:
		f = input("請輸入文字: ")
		if f == "q":
			n.write("\n")
			break		
		n.write(f)
		n.write("\n")

with open("name.txt", "r", encoding = "utf-8") as n:
	for line in n:
		print(line.strip())