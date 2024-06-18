def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words into a new sentence
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Input sentence
sentence = input("Enter the sentence")
# Call the function and print the result
print(reverse_words(sentence))
