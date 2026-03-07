def Reverse_String(s: str) -> str:
      reversed_str = ""
      for i in range(len(s)):
            reversed_str += s[len(s)-1-i]
      return reversed_str

if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))






