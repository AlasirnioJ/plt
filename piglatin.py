class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        if self._phrase == "":
            return "nil"
        return self._phrase

    def translate(self) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        separator = " "
        if "-" in self._phrase:
            separator = "-"
        phrases = self._phrase.split(separator)
        return_string = ""
        for phrase in phrases:
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
                    return_string +=  phrase[index:] + start + "ay" + separator
                    continue
                start = phrase[1:]
                return_string +=  start + phrase[0]  + "ay"+ separator
                continue

            if ending == "y":
                return_string +=  phrase + "nay" + separator
                continue
            if ending in vowels:
                return_string +=  phrase + "nay" + separator
                continue
            return_string += phrase + "ay" + separator
            continue
        if return_string[-1] == " " or return_string[-1] == "-":
            return_string = return_string[:-1]
        return return_string
