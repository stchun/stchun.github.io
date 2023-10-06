# decript.py

special_char = [' ', '.', ',', '!', '?', '~']
def char_tokenize(str):
    char_list = []
    word_index = 1
    for word in str.split('#'):
        for char in word.split('*'):
            sp = ''

            for ch in char:
                if ch in special_char:
                    sp = ch

            if sp == '':
                char_list.append(char)
            else:
                index = 1
                sp_list = char.split(sp)

                for tok in sp_list:
                    if len(tok) > 0:
                        char_list.append(tok)

                    if index < len(sp_list):
                        char_list.append(sp)
                    index += 1

        if word_index < len(str.split('#')):
            char_list.append(' ')
        word_index += 1
        
    return char_list