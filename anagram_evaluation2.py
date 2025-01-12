from collections import Counter

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare character counts
    return Counter(str1) == Counter(str2)

# Test cases
print(are_anagrams("Listen", "Silent"))  # True
print(are_anagrams("Hello", "Olelh"))    # True
print(are_anagrams("Python", "Java"))    # False