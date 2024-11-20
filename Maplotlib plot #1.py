from matplotlib import pyplot as plt


#print(plt.style.available) - всі стилі
plt.style.use('ggplot')

#plt.xkcd() - крива хуйня   пздц

dev_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_dev_y = [38496, 28934, 12345, 20839, 23456,
         13934, 29088, 89223, 78234, 18920]

second_dev_y = [12902, 15249, 24359, 33333, 34082,
                17829, 26897, 30000, 79287, 127289]

plt.plot(dev_x, first_dev_y, "m--.", label= "First")

plt.plot(dev_x, second_dev_y, color = "#444444", marker = '.', linestyle = '-', linewidth = 3, label = "Second")

plt.xlabel('Age')
plt.ylabel("Random numbers used")

plt.title("First Random Graph")

plt.legend()

plt.tight_layout()

plt.grid(True) #- сітка

plt.show()