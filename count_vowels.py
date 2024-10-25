def count_vowels(string):
    #define a set containing all vowel letters
    vowels = set("aeiouAEIOU")

    #intialise vowel counter to 0
    counter = 0

    for char in string:
        if char in vowels:
            counter +=1

    return counter


input_string = "Lemi"
vowel_count = count_vowels(input_string)
print(f"Number of vowels in '{input_string}': {vowel_count}")

