str=input("Enter the word")
word=str.split()
Largest=small=word[0]
Longest_Word_Length=len(word[0])



for i in range(0,len(word)):
    if len(Largest)<len(word[i]):
        Largest=word[i]

    if len(small)>len(word[i]):
        small=word[i]
        Smallest_Word_Length= len(small)
print("The Largest word in the sentence is :", Largest)
print("Length of the Longest word is :", Longest_Word_Length)
print("The smallest word in the sentece is :",small)
print("Length of smallest is  ", Smallest_Word_Length)
