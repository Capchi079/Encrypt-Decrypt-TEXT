class TextCaesar:
    key = int(input('Enter a key: '))#if the enter value is zero then it will not perform
    if key >=1:
            def encrypt(self,key=key):
                    enc_list = []
                    for values in self.text:
                        ASCII = int(ord(values))
                        enc_list.append((ASCII + key) % 256)
                    Plan_text = ''.join(chr(i) for i in enc_list)
                    print('The encrypt  message is: "' + Plan_text + '"')
    else:
        print("enter number is not correct")
    def __init__(self):
        self.text = input('Enter The message: ')
    def decrypt(self,key=key):
        k= int(input("for Verification enter the same number before you encrypt the message:  "))
        if key == k:
                print(self.text)
        else:
            print("Enter number not matched can't Decrypt")
saty=TextCaesar()
saty.encrypt()
saty.decrypt()