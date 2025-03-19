import random
import string
def generate_password(length):
    all_characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(all_characters)for _ in range(length))
    return password
def main():
    length=int(input("enter a desired length of a password:"))
    password=generate_password(length)
    print(f"Generated password:{password}")
if __name__=="__main__":
    main()