import random

# 1. Math Engine: Handles different physics formulas
def physics_calculator(theme, val1, val2):
    if theme == "Force":
        # F = m * a
        return val1 * val2
    elif theme == "Velocity":
        # V = d / t
        return round(val1 / val2, 2)
    elif theme == "Energy":
        # E = m * c^2 (Simplified for the game as E = val1 * val2)
        return val1 * val2
    return 0

# 2. Validation Engine: Checks the user's input (If/Else requirement)
def validate_result(user_input, actual_value):
    if user_input == actual_value:
        print("🌟 Brilliant! Your calculations are spot on.")
        return True
    else:
        print(f"⚠️ Calculation error. The expected value was {actual_value}.")
        return False

# 3. Game Engine: Manages the 10 questions (Loop requirement)
def run_physics_test():
    score = 0
    themes = ["Force", "Velocity", "Energy"]
    
    print("🔬 Welcome to the Multi-Theme Physics Assessment 🔬")
    print("--------------------------------------------------")

    # Loop for 10 questions
    for i in range(1, 11):
        current_theme = random.choice(themes)
        val1 = random.randint(5, 20)
        val2 = random.randint(1, 5)
        
        correct_answer = physics_calculator(current_theme, val1, val2)
        
        print(f"\nQuestion {i}: [{current_theme}]")
        if current_theme == "Force":
            print(f"Find Force (N) if Mass = {val1}kg and Acceleration = {val2}m/s²")
        elif current_theme == "Velocity":
            print(f"Find Velocity (m/s) if Distance = {val1}m and Time = {val2}s")
        elif current_theme == "Energy":
            print(f"Find Potential Energy (J) if Mass*Gravity = {val1} and Height = {val2}m")

        try:
            user_ans = float(input("Enter your answer: "))
            if validate_result(user_ans, correct_answer):
                score += 1
        except ValueError:
            print("❗ Invalid input. Please enter numbers only.")

    print(f"\n--- Final Results ---")
    print(f"Total Score: {score}/10")

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    run_physics_test()