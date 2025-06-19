import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
Y = [20, 25, 35, 50, 10, 12, 20, 40, 70, 110]
#plt.plot(X, Y) #- рисуем график
#plt.show()  #- это команда вывести график на экран
plt.plot(X, Y)  # Построить график зависимости y от x
plt.title("Линейный график")
plt.xlabel("X")
#plt.ylabel("Y")
plt.show()
