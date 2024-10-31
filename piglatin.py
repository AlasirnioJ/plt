class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        if self._phrase == "":
            return "nil"
        return self._phrase

    def translate(self) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        phrases = self._phrase.split(" ")
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
                            continue
                    start = phrase[:index]
                    return_string +=  phrase[index:] + start + "ay "
                    continue
                start = phrase[1:]
                return_string +=  start + phrase[0]  + "ay "
                continue

            if ending == "y ":
                return_string +=  phrase + "nay "
                continue
            if ending in vowels:
                return_string +=  phrase + "nay "
                continue
            return_string += phrase + "ay "
            continue
        if return_string[-1] == " ":
            return_string = return_string[:-1]
        return return_string
