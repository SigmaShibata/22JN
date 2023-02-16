text = list(input("文字列を入力 --> "))
i = 0
while True:
    count = 1
    while True:
        if i < len(text) - 1 and text[i] == text[i + 1]:
            text.pop(i)
            count += 1
        else:
            break
    text.insert(i+1, str(count))
    i += 2
    if i >= len(text) -1:
        if count == 1:
            text.insert(i+1, str(count))
        break
for s in text:
    print(s, end="")