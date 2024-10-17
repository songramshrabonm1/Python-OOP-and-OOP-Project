def call():
    print('Calling someone i don\'t know')
    return 'call done'

class phone : 
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camer', 'speaker','hammer']

    def call(self):
        print('calling one person')

    def send_sms(self,phone , sms):
        text = f"sending sms to : {phone} and message : {sms}"
        return text




my_phone = phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(4152 , ' i forgot to miss you ')
print(result)