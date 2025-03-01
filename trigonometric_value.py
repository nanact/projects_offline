import math

def calculate_trigonometric_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)

    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)
    
    return sine_value, cosine_value, tangent_value

angle_degrees = float(input("Enter the angle in degrees: "))

sine, cosine, tangent = calculate_trigonometric_values(angle_degrees)

print(f"Sine({angle_degrees}°) = {sine}")
print(f"Cosine({angle_degrees}°) = {cosine}")
print(f"Tangent({angle_degrees}°) = {tangent}")
