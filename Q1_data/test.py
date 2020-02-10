import pickle 

example_dict = {1:"6",2:"2",3:"f"}

import matplotlib.pyplot as plt

# pickle_out = open(data.pkl, "wb")

# pickle.dump(example_dict, pickle_out)

# pickle_out.close()



pickle_in = open("data.pkl","rb")
example_dict = pickle.load(pickle_in)

# plt.plot(example_dict)

x_var = [] 
y_var = []

for a in example_dict:
	x_var.append(a[0])
	y_var.append(a[1])

plt.plot(x_var , y_var)


print(example_dict)
print(len(example_dict))

plt.show()
