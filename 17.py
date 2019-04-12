num_lookup = {"0": "",
"1": "one",
"2": "two",
"3": "three",
"4": "four",
"5": "five",
"6": "six",
"7": "seven",
"8": "eight",
"9": "nine",
"00": "",
"10": "ten",
"11": "eleven",
"12": "twelve",
"13": "thirteen",
"14": "fourteen",
"15": "fifteen",
"16": "sixteen",
"17": "seventeen",
"18": "eighteen",
"19": "nineteen",
"20": "twenty",
"30": "thirty",
"40": "forty",
"50": "fifty",
"60": "sixty",
"70": "seventy",
"80": "eighty",
"90": "ninety",
"100": "hundred",
"1000": "thousand"}

def num2word(x:int) -> str:
    x_str = str(x)
    s = ""
    if len(x_str) == 4:
        s += num_lookup[x_str[:1]]
        s += num_lookup["1000"]
    if len(x_str) == 3:
        s += num_lookup[x_str[:1]]
        s += num_lookup["100"]
        if x_str[1:] != "00":
            s += "and"
            if x_str[1:2] != "1":
                s += num_lookup[x_str[1:2] + "0"]
                s += num_lookup[x_str[2:]]
            else:
                s += num_lookup[x_str[1:]]

    if len(x_str) == 2:
        if x_str[0:1] != "1":
            s += num_lookup[x_str[0:1] + "0"]
            s += num_lookup[x_str[1:]]
        else:
            s += num_lookup[x_str]
    if len(x_str) == 1:
        s += num_lookup[x_str]
    return s

count = 0
for i in range(1,1000 + 1):
    count += len(num2word(i))
    print(len(num2word(i)), num2word(i))
print(str(count))