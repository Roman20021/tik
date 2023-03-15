alph_len = int(input('Длина алфавита:'))
codes = {}
for i in range(alph_len):
    code_pair = input().split()
    print(code_pair)
    codes[code_pair[1]] = code_pair[0]
print('input message')
message = input()

result = ''
while len(message) > 0:
    for code in codes:
        if message.startswith(code):
            result += codes[code]
            message = message[len(code):]
            break
print(result)