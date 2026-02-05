# decision_maker.py
# This program helps the user decide the best study method
# based on subject, available time, and learning style

print("Welcome to the study method decision-maker!📚")

# Ask the user questions

subject = input(" What subject are you studying? (math / biology / language): ")
time = int(input("How many minutes do you have to study? "))
style = input("what is your learning style? (visual/ auditory / reading): ")

print("\n🤔 Thinking about the best study method for you...\n")
 
#Decision logic using if,elif and else

if time < 30:
  # Short study recommendations
  if style == "visual":
    recommendation = "Watch a short video or review diagrams"
  elif style == "auditory":
    recommendation = "Listen to a quick explanation or aduio notes."
  else:
    recommendation = "Reas summaries or key points."

elif 30 <= time <= 90:
  #medium  study time recommendations
  if subject == "math":
    recommendation = "Practice problems step by step."
  elif subject == "biology":
    recommendation = "study diagrams and make simple notes"
  else:
    recommendation = "Practice vocabulary and example sentences"
else:

  # Long study time recommendations
    recommendation = "Do a full study session: review notes. practice, and self-test"
  #FINAL OUTPUT
print("✅ Recommendation:")
print(recommendation)
print("\nGood luck with your studies! 💪📖")