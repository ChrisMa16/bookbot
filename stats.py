def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def char_count(file_contents):
    char_dict = {}
    text = file_contents
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1
    return char_dict


def list_dict(char_dict):
    dict_list = []
    new_dict = {}
    for char, count in char_dict.items():
        new_dict = {"char":char,"num":count}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True,key=sort_on)
    return dict_list

def sort_on(items):
    return items["num"]
