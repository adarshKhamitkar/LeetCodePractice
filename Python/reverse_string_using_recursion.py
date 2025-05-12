names_list = ["Adarsh", "Yashaswi", "Naman"]

def reverse_string(name):
    if len(name)==0:
        return name
    else:
        return name[-1]+reverse_string(name[:-1])

def main():
    for name in names_list:
        reverse_name = reverse_string(name)
        print(name.lower() + "   " + reverse_name.lower())
        if name.lower() == reverse_name.lower():
            print("name "+name+" is palindrome")
        else:
            print("name "+name+" is not palindrome")

if __name__ == "__main__":
    main()