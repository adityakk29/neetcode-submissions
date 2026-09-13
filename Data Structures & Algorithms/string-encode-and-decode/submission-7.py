class Solution:

    def encode(self, strs: List[str]) -> str:
        return str(len(strs)) + '#' + '|'.join(
            ['%'.join([str(ord(ch) + 11) for ch in elem]) for elem in strs]
        )

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []

        count, encoded = s.split('#', 1)

        if int(count) == 0:
            return []

        elem_list = encoded.split('|')

        return [
            ''.join([chr(int(ch) - 11) for ch in elem.split('%')])
            if len(elem) > 0 else ""
            for elem in elem_list
        ]