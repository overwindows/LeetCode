class Solution:
    def interpret(self, command: str) -> str:
        cmd0 = command.replace("()","o")
        cmd1 = cmd0.replace("(al)","al")
        return cmd1
            