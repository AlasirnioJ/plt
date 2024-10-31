class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        if self._phrase == "":
            return "nil"
        return self._phrase

    def translate(self) -> str:
        vowels = ["a", "e", "i", "o", "u", "y"]
        ending = self._phrase[-1]
        if ending in vowels:
            return self._phrase + "nay"
