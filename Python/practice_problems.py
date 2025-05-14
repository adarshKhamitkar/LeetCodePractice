def recursive_reverse_string(s):
    if len(s) == 0: return s
    else: return s[-1] + recursive_reverse_string(s[:-1])

def is_palindrome(s) -> bool:
    if s == recursive_reverse_string(s): return True
    return False

def word_count(statement: str) -> dict:
    word_counter = dict()
    for word in statement.split():
        word_counter[word] = word_counter.get(word, 0) + 1 
    return word_counter
    
def main():
    statement = "sampagappa na maga mari sampagappa"
    print(word_count(statement))
    
if __name__ == "__main__":
    main()
    