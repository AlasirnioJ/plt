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
            start = self._phrase[1:]
            return start + self._phrase[0]  + "ay"


        if ending == "y":
            return self._phrase + "nay"
        if ending in vowels:
            return self._phrase + "nay"
        return self._phrase + "ay"
