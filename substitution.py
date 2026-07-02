# Figure 2: S-Box Substitution Logic
def s_box_layer(input_val):
    # Mapping based on Week 6 Class Demonstration 1
    s_box = {0:14, 1:4, 2:13, 3:1}
    
    # Logic to show the substitution
    output = s_box.get(input_val, "Invalid Input")
    return output

print("--- S-Box Substitution ---")
input_data = 2
result = s_box_layer(input_data)
print(f"Input: {input_data} -> Output: {result}")