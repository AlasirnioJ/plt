from curses.ascii import isupper


class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        if self._phrase == "":
            return "nil"
        return self._phrase

    def translate(self) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        punctuations = [".", "?", "!"]

        punctuation = ""
        separator = " "
        if "-" in self._phrase:
            separator = "-"
        phrases = self._phrase.split(separator)
        return_string = ""
        for phrase in phrases:

            isupper = phrase.isupper()

            if phrase[-1] in punctuations:
                    punctuation = phrase[-1]
                    ending = phrase[-2]
                    phrase = phrase[:-1]
            else:
                ending = phrase[-1]

            if phrase[0] not in vowels:
                if phrase[1] not in vowels:
                    index = 0
                    for char in phrase:
                        if char not in vowels:
                            index += 1
                        else:
                            break
                    start = phrase[:index]
                    returnable = phrase[index:] + start + "ay" + punctuation  + separator
                    if isupper:
                        returnable = returnable.upper()
                    return_string +=  returnable
                    continue
                start = phrase[1:]
                returnable =  start + phrase[0]  + "ay" + punctuation + separator
                if isupper:
                    returnable = returnable.upper()
                return_string += returnable
                continue

            if ending == "y":
                returnable =  phrase + "nay" + punctuation  + separator
                if isupper:
                    returnable = returnable.upper()
                return_string += returnable
                continue
            if ending in vowels:
               returnable = phrase + "yay" + punctuation + separator
               if isupper:
                    returnable = returnable.upper()
               return_string += returnable
               continue
            returnable = phrase + "ay" + punctuation + separator
            if isupper:
                returnable = returnable.upper()
            return_string += returnable
            continue
        if return_string[-1] == " " or return_string[-1] == "-":
            return_string = return_string[:-1]
        return return_string
