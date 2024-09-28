def to_jaden_case(string):
    new_lst = [word[0].upper() + word[1:] for word in string.split()] 
    s = ' '.join(new_lst)
    return s