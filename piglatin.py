class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        if self._phrase == "":
            return "nil"
        return self._phrase

    def translate(self) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        ending = self._phrase[-1]



        if self._phrase[0] not in vowels:
            if self._phrase[1] not in vowels:
                index = 0
                for char in self._phrase:
                    if char not in vowels:
                        index += 1
                    else:
                        break
                start = self._phrase[:index]
                print("start", start)
                return self._phrase[index:] + start + "ay"
            start = self._phrase[1:]
            return start + self._phrase[0]  + "ay"


        if ending == "y":
            return self._phrase + "nay"
        if ending in vowels:
            return self._phrase + "nay"
        return self._phrase + "ay"
