import matplotlib.pyplot as plt

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
numWeb = [376, 348, 153, 104, 19]
explode = (.1, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
wedgeColors = ("midnightblue", "darkblue", "blue", "royalblue", "cornflowerblue")
ax1.pie(numWeb, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=135, colors = wedgeColors)
ax1.axis('equal')
plt.suptitle("Popular Graphic Formats")

plt.show()