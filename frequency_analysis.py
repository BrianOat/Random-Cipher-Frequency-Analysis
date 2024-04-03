# Prompt user input
ciphertxt = input("Enter Cipher Text: ")

# Calculate the frequency of each letter in the cipher text using a dictionary
freq={}
for char in ciphertxt:
    if not isalph(char):
        continue
    if char not in freq:
        freq[char]=1
    else:
        freq[char]+=1


# Most Frequent letters in the english language stored in a list.
# 0 index indicates MOST frequent
mostFreqEnglish= ["E", "T", "A", "O", ""]

# set of worda to match against
