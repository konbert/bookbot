
def count_words(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    chars = {}
    
    text = text.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(dict):
    return dict["count"]

def sort_chars(dict):
    sorted_chars = []
    for char in dict:
        sorted_chars.append({"char": char, "count": dict[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
