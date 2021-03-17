import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = []

for num in input_values:
    cubes.append(num*num*num)

plt.style.use("seaborn-white")
ax1 = plt.subplot(1, 2, 1)
ax1.plot(input_values, cubes, marker="D", ls="dashed", c="green")

ax1.set_title("Cubed Numbers", fontsize=24)
ax1.set_xlabel("Value", fontsize=14)
ax1.set_ylabel("Cube of Value", fontsize=14)

ax1.tick_params(axis='both', labelsize=14)


raised = []

for num in input_values:
    raised.append(num**2)

plt.style.use("seaborn")
ax2 = plt.subplot(1, 2, 2)
ax2.plot(input_values, raised, marker="*", ls="dotted", c="orange")

ax2.set_title("Numbers Raised", fontsize=24)
ax2.set_xlabel("Value", fontsize=14)
ax2.set_ylabel("Second Power", fontsize=14)

ax2.tick_params(axis='both', labelsize=14)

plt.suptitle("Fun with Graphs",c="blue",fontfamily="Comic Sans MS", fontsize="20")
plt.subplots_adjust(top=.8,wspace=1)

plt.show()