class TextEditor:
    def __init__(self, initial_string:str=""):
        self.current_str = list(initial_string)
        self.stack = []
    def append(self,s: str):
        self.stack.append("".join(self.current_str))
        self.current_str.extend(s)
    def delete(self,k: int):
        self.stack.append("".join(self.current_str))
        self.current_str = self.current_str[:-k]
    def print(self, k:int):
        print(self.current_str[k-1])
    def undo(self):
        if self.stack:
            self.current_str = list(self.stack.pop())
    def command(self, s:str):
        parts = s.split(maxsplit=1)
        op = int(parts[0])

        if op == 1:
                self.append(parts[1])
        elif op == 2:
                self.delete(int(parts[1]))
        elif op == 3:
            self.print(int(parts[1])) 
        elif op == 48: 
            self.undo()

if __name__ == "__main__": 
    Q = int(input()) 
    editor = TextEditor() 
    for _ in range(Q): 
        command = input().strip() 
        editor.command(command)