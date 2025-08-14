# def highest_Frequency(s):
#     max_frequency = 0
#     current_frequency = 1
#     result_chars = []
    
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             current_frequency += 1
#         else:
#             if current_frequency > max_frequency:
#                 max_frequency = current_frequency
#                 result_chars = [s[i - 1]]
#             elif current_frequency == max_frequency:
#                 result_chars.append(s[i - 1])
            
#             current_frequency = 1  # Reset count for new character

#     # Handle last character sequence
#     if current_frequency > max_frequency:
#         max_frequency = current_frequency
#         result_chars = [s[-1]]
#     elif current_frequency == max_frequency:
#         result_chars.append(s[-1])

#     return max_frequency, result_chars

# # Example usage
# s = "aaaacccccccddddaaaaaa"
# print(highest_Frequency(s))


def highest_Frequency(s):
    char_map = {}  # Dictionary to store max consecutive occurrences per character
    max_frequency = 0  
    current_frequency = 1  

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  
            current_frequency += 1  
        else:
            # Update the character's max frequency in the dictionary
            char_map[s[i - 1]] = max(char_map.get(s[i - 1], 0), current_frequency)
            
            # Update overall max frequency
            max_frequency = max(max_frequency, char_map[s[i - 1]])

            current_frequency = 1  # Reset for new character
    
    # Handle the last sequence
    char_map[s[-1]] = max(char_map.get(s[-1], 0), current_frequency)
    max_frequency = max(max_frequency, char_map[s[-1]])

    # Find all characters with the max frequency
    result_chars = [char for char, freq in char_map.items() if freq == max_frequency]

    return max_frequency, result_chars

# Example usage
s = "aaaacccccccddddaaaaaaa"
print(highest_Frequency(s))
