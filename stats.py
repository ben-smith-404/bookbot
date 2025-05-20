def get_num_words(content):
    number_of_words = len(content.split())
    return number_of_words

def count_character_occurance(content):
    tracking_dict = {}
    for char in content:
        char =str.lower(char)
        if char in tracking_dict:
            tracking_dict[char] += 1
        else:
            tracking_dict[char] = 1
    return tracking_dict

def sort_character_dictionary(dictionary):
    sorted_list = []
    for key in dictionary:
        temp_dict = {"char": key, "num": dictionary[key]}
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]