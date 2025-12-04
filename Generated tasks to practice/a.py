input = "aaadddddffggggghhj"

compressed = ""

counter = 1

for i in range(1, len(input)):
    if input[i] == input[i-1]:
        counter += 1
    
    else:
        compressed += input[i-1] + str(counter)
        counter = 1
        
compressed += input[-1] + str(counter)

print(compressed)
    