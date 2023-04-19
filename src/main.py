from datagen.walker import Walker

bert = Walker()

for i in range(8):
    bert.walk()
    print(bert.pos)



