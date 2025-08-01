import re


# 🧩 Challenge 1: Nigerian Phone Numbers (Harder Version)
# 📋 Task:
# Extract only valid Nigerian phone numbers that:
#
# Start with 080, 081, 090, 070
#
# Are exactly 11 digits long

# 🧩 Challenge 2: Find All Capitalized Words
# 📋 Task:
# Match all words that start with a capital letter (e.g., names, places).

# 🧩 Challenge 3: Extract Dates (dd-mm-yyyy or dd/mm/yyyy)
# 📋 Task:
# Find all dates in the form of 12-06-2025 or 12/06/2025

# 🧩 Challenge 4: Find All Sentences Ending with a Question Mark
# 📋 Task:
# Match complete questions (i.e., sentences ending with ?)

# 🧩 Challenge 5: Match Twitter Handles Only
# 📋 Task:
# Extract valid Twitter handles that:
#
# Start with @
#
# Are followed by 3 or more characters (letters, digits, or underscore)


# CHALLENGE 1
text = "Call me on 08142353738 or 07034567891. Ignore 06098765432, 1234567890, and 0801234567."
result =  re.findall(r"0[789][01]\d{8}", text)

print(result)

# CHALLENGE 2
text2 = "My friends John and Mary visited Nigeria and met Elon Musk."
result2 = re.findall(r"\b[A-Z][a-z]\w+", text2)
print(result2)

# CHALLENGE 3
text3 = "Our meetings are on 12/06/2025, 25-12-2025, and 01/01/2024."
result3 = re.findall(r"\d{2}[-/]\d{2}[-/]\d{4}", text3)
print(result3)

#CHALLENGE 4
text4 = "How are you? I am fine. Where is your bag? This is not a question"
result4 = re.findall(r"[^.?!]*\?", text4)
print(result4)

#CHALLENGE 5
text5 = "Follow @dev_celestine, @OpenAI, and @ab but not @@wrong or @1!"
result5 = re.findall(r"@\w{3,}", text5)
print(result5)
