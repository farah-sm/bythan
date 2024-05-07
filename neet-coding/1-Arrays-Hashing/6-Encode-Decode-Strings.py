# String Manipulation

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return None
        return "-encoded-str".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s.split("-encoded-str")
