message = "python running"
print(message.upper())
print(message.lower())

bicycles = ['trek', 'cannondale', 'redline']
print(bicycles)
for bike in bicycles:
    print(bike)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

for i in range(0,100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
