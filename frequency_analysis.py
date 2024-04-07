# Prompt user input
ciphertxt = input("Enter Cipher Text: ")

# Calculate the frequency of each letter in the cipher text using a dictionary
freq={}
for char in ciphertxt:
    if not char.isalpha():
        continue
    if char not in freq:
        freq[char]=1
    else:
        freq[char]+=1


# Most Frequent letters in the english language stored in a list.
# 0 index indicates MOST frequent
mostFreqEnglish= ["E", "T", "A", "O", "I", "N", "S", "R", "H", "D", "L", "U", "C", "M", "F", "Y", "W", "G", "P", "B", "V", "K", "X", "Q", "J", "Z"]
#print(len(mostFreqEnglish))

most=0
i=0
replacedText=""
sortedFreq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

# Output the sorted dictionary
print(sortedFreq)
for key in sortedFreq:
    if i==0:
        print(f"The most frequent letter in the ciphertext is: {key}, therefore replacing it with the most frequent letter in the english language (e) gives us:")
        replacedText = ciphertxt.replace(key, 'E')
        print(replacedText)
    else:
        print(f"The next most frequent letter in the ciphertext was: {key}, therefore replacing it with " + mostFreqEnglish[i] + " is now:")
        replacedText = replacedText.replace(key,mostFreqEnglish[i])
        print(replacedText)
    i+=1

# set of words to match against
