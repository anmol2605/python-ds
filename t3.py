from turtle import*
speed('fastest')
colors = ['red','purple','blue','green']
pensize(2)
for i in range(100):
    pencolor (colors[i%4])
    fd(i*2) #fd(i*2)lt(60),fd(i*5)lt(90)
    lt(60)
    circle(i*2, 90)

mainloop()