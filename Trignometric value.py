import math
import random

# Generate a random angle between 0 and 360 degrees
angle_deg = random.randint(0, 360)
print(f"Randomly selected angle: {angle_deg}°")

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate trigonometric values
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)

# Tan can blow up at 90, 270 so,
try:
    tan_val = math.tan(angle_rad)
except:
    tan_val = "Undefined"

# Display results
print(f"sin({angle_deg}°) = {sin_val:.4f}")
print(f"cos({angle_deg}°) = {cos_val:.4f}")
print(f"tan({angle_deg}°) = {tan_val if isinstance(tan_val, str) else round(tan_val,4)}")
#Finished!😊