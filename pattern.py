


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# def split_string_into_words(text):
#     words = []
#     word = ""
    
#     for char in text:
#         if char.isspace():
#             if word:
#                 words.append(word)
#                 word = ""
#         else:
#             word += char
    
#     if word:
#         words.append(word)
    
#     return words

# text = "Split a string into a list of words"
# word_list = split_string_into_words(text)
# print(word_list)



def reverse_order(str3):
    words=str3.split()
    reverse_word=words[::-1]
    reversed_string=" ".join(reverse_word)
        
    return reversed_string

str3="studying is the ke to success"
a=(reverse_order(str3))

print(a)