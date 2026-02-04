class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        buffer = ""

        for line in source:
            i = 0
            if not in_block:
                buffer = ""

            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    
                    break
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                   
                    in_block = True
                    i += 2
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                   
                    in_block = False
                    i += 2
                elif not in_block:
                    buffer += line[i]
                    i += 1
                else:
                    i += 1

            if not in_block and buffer:
                res.append(buffer)

        return res