
# n = int(input())
# arr = []
# result = []

# for i in range(n):
#     arr.append(i + 1)
#     result.append(arr.copy())

# print(*result, sep="\n")

chars = input()
step = 1
buf = "test string"
out = [[]]

while step <= len(chars):
    for i in range(len(chars)):
        if i + step > len(chars):
            break
        out.append([ char for char in chars[i:i+step] ])
    step += 1
print(out)
