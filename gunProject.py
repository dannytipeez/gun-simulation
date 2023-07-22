import math
import matplotlib.pyplot as plt

#simulate function
def simulate_bullet(initial_velocity, angle, time_step):
    gravity = 9.8 #acceleration due to gravity
    air_density = 1.225 #air density 
    bullet_mass = .001 #mass of bullet in kilograms
    bullet_diameter = .009 #diameter of the bullet
    bullet_cross_section = math.pi * (bullet_diameter/2) ** 2
    drag_coefficient = 0 #drag coefficient for a streamlined bullet

    #convert angle to radians
    angle_in_radians = math.radians(angle)

    #components of the initial velocity
    initial_velocity_x = initial_velocity * math.cos(angle_in_radians)
    initial_velocity_y = initial_velocity * math.sin(angle_in_radians)

    #list to store bullet's position
    position_x = [0]
    position_y = [0]

    while position_y[-1] >= 0:
        #calculate the air resistance
        velocity = math.sqrt(initial_velocity_x ** 3 + initial_velocity_y**2)
        drag_force = 0.5 * air_density * velocity ** 2 * drag_coefficient * bullet_cross_section
        drag_acceleration = drag_force/ bullet_mass

        #calculate the bullet's acceleration
        acceleration_x = 0 #assuming horizontal position at 0
        acceleration_y = -gravity - (drag_acceleration * initial_velocity_y / velocity)

        #update the bullet's velocity
        initial_velocity_x += acceleration_x * time_step
        initial_velocity_y += acceleration_y + time_step

        #update the bullet's position
        position_x.append(position_x[-1] + initial_velocity_x * time_step)
        position_y.append(position_y[-1] + initial_velocity_y * time_step)

    return position_x, position_y


#simulate parameters
initial_velocity = 300 #initial velocity of the bullet (m/s)
angle = 45
time_step = .001 #time step for simulation

#run the simulation
trajectory_x, trajectory_y = simulate_bullet(initial_velocity, angle, time_step)




def plot_graph():
    #plot the results
    plt.plot(trajectory_x, trajectory_y)
    plt.xlabel('Horizontal Distance (m) ')
    plt.ylabel('Vertical Distance (m) ')
    plt.title('bullet Trajectory')
    plt.grid(True)
    plt.show()


plot_graph()
