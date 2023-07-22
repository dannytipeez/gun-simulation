import math
import matplotlib.pyplot as plt

def calculate_bullet_trajectory(initial_velocity, angle, mass, bullet_diameter):
    # Constants
    air_density = 1.225  # kg/m^3 (standard air density at sea level)
    drag_coefficient = 0.5  # coefficient of drag for a typical bullet
    gravitational_acceleration = 9.8  # m/s^2

    # Convert angle to radians
    angle = math.radians(angle)

    # Calculate initial conditions
    initial_velocity_x = initial_velocity * math.cos(angle)
    initial_velocity_y = initial_velocity * math.sin(angle)
    initial_position_x = 0
    initial_position_y = 0

    # Calculate time step and total time
    time_step = 0.01  # seconds (adjust as needed for accuracy)
    total_time = 2 * initial_velocity_y / gravitational_acceleration

    # Initialize variables
    current_time = 0
    current_position_x = initial_position_x
    current_position_y = initial_position_y
    current_velocity_x = initial_velocity_x
    current_velocity_y = initial_velocity_y

    # Lists to store trajectory points
    trajectory_x = []
    trajectory_y = []

    while current_time <= total_time:
        # Update positions
        current_position_x += current_velocity_x * time_step
        current_position_y += current_velocity_y * time_step

        # Calculate forces
        drag_force_x = -0.5 * air_density * math.pi * (bullet_diameter/2)**2 * drag_coefficient * current_velocity_x * abs(current_velocity_x)
        drag_force_y = -0.5 * air_density * math.pi * (bullet_diameter/2)**2 * drag_coefficient * current_velocity_y * abs(current_velocity_y)
        gravitational_force = mass * gravitational_acceleration

        # Calculate accelerations
        acceleration_x = (drag_force_x) / mass
        acceleration_y = (drag_force_y - gravitational_force) / mass

        # Update velocities
        current_velocity_x += acceleration_x * time_step
        current_velocity_y += acceleration_y * time_step

        # Update time
        current_time += time_step

        # Add current position to the trajectory
        trajectory_x.append(current_position_x)
        trajectory_y.append(current_position_y)

    return trajectory_x, trajectory_y

# Example usage
initial_velocity = 100  # m/s
angle = 4  # degrees
mass = 0.01  # kg
bullet_diameter = .001  # m

trajectory_x, trajectory_y = calculate_bullet_trajectory(initial_velocity, angle, mass, bullet_diameter)

# Plotting the trajectory
plt.plot(trajectory_x, trajectory_y)
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Bullet Trajectory')
plt.grid(True)
plt.show()
