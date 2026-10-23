class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []
        for word in strs:
            pieces.append(f"{len(word)}#{word}")
        return "".join(pieces)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0  # start of the current length label

        while i < len(s):
            # 1) Find the '#' that ends the length label.
            #    The label is only digits, so the first '#' is the separator.
            j = i
            while s[j] != "#":
                j += 1

            # 2) Parse the length.
            length = int(s[i:j])

            # 3) Take exactly `length` characters after '#'.
            #    We never inspect these, so any character (even '#') is safe.
            word_start = j + 1
            result.append(s[word_start:word_start + length])

            # 4) Jump to the next label.
            i = word_start + length

        return result
