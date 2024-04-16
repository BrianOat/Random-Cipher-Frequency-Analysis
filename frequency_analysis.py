# Prompt user input
ciphertxt = input("Enter Cipher Text: ")

# Calculate the frequency of each letter in the cipher text using a dictionary
freq = {}
for char in ciphertxt:
    if not char.isalpha():
        continue
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] += 1

# Most Frequent letters in the english language stored in a list.
# 0 index indicates MOST frequent
mostFreqEnglish = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "D", "L", "U", "C", "M", "F", "Y", "W", "G", "P", "B", "V", "K", "X", "Q", "J", "Z"]

# Sort the frequencies
sortedFreq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

# Output the sorted dictionary
print(sortedFreq)

replacedText = ciphertxt  # Initialize replacedText with the original ciphertext


# Perform automated partial decryption
for i, key in enumerate(sortedFreq): #i = position in list of most frequent english letters, key is 
    if i == 0:
        print(f"The most frequent letter in the ciphertext is: {key}, therefore replacing it with the most frequent letter in the English language (E) gives us:")
        replacedText = replacedText.replace(key, 'E')
        print(replacedText)
    else:
        print(f"The next most frequent letter in the ciphertext was: {key}, therefore replacing it with {mostFreqEnglish[i]} is now:")
        replacedText = replacedText.replace(key.lower(), mostFreqEnglish[i])
        print(replacedText)

# Manual replacement by the user
print("\nEnter manual replacements:")
print("Enter 'quit' to finish.")
while True:
    original = input("Original letter: ")
    if original.lower() == 'quit':
        break
    replacement = input("Replacement letter: ")
    replacedText = replacedText.replace(original.upper(), replacement.lower())
    print(replacedText)

# Output fully decrypted text
print("\nFully decrypted text:")
print(replacedText.upper())
