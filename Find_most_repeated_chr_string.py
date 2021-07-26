sentence = "This is a common interview question"

count_chr = {}

for chr in sentence:
    if chr in count_chr:
        count_chr[chr] += 1 
    else:
        count_chr[chr] = 1 
    
char_freq_sorted = sorted(count_chr.items(), key=lambda kv:kv[1], reverse = True) 
print(char_freq_sorted[0])
