age_as_text = "15"
age_as_number = int(age_as_text)      # str -> int

pi_text = "3.14159"
pi_number = float(pi_text)            # str -> float

score = 92
score_text = str(score)               # int -> str

print("1. Type conversion")
print(age_as_number + 1)              # works: it's a real int now
print(pi_number * 2)
print("Score: " + score_text)         # works: both are strings now

#print(score_text +1)#                # doesn't work: only concentrate str (not "int) to str
# type doesn't match
