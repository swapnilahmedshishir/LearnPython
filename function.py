def my_funtion():
    print('hello from a function')
my_funtion()


def childName(*kids):
    print(f'The youngest child is {kids[2]}')
childName('swapnil' , 'ahmmed','shihsir')

fruits=['apple', 'banana', 'pinaple']

def list_funtion(food):
    for x in food:
        print(x)


list_funtion(fruits)