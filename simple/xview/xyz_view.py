import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_proj_type('ortho')
ax.view_init(elev=30, azim=30)
ax.set_box_aspect([1,1,1])
plt.show()
