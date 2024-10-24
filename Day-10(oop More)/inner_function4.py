#function is first class object
def double_decker():
    print('Starting the double decker')
    def inner_fun():
        print('Inside the inner')
        return 300
    return inner_fun


print(double_decker())# amader eTa ekta function tahole . ar ekhane ei function er vitor er theke return korteche abar inner_fun . tahole ekhane print korbe print() funtion ta ke ja double_decker() function er vitore ache ta . ebong tar vitore je inner_fun() ache sei function ta return korbe . 

# amra zodi chai double_decker() function er vitore er inner_fun() ke o call korte chai tahole ta ke amra evabe call dite pari 
print(double_decker()())


# **************************************************#

def do_something(work):
    print('work started')
    work()
    print('work ended')

# do_something(2)
# do_something('ami busy')

def coding():
    print('Coding in python')

do_something(coding)