import time
def calc():
    product=1
    for i in range(1,100000):
        product=product*i
    return product

start=time.time()
prod=calc()
end=time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (end - start))
