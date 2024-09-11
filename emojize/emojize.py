# importing emoji module
import emoji
# getting input from user
emo = input("Input: ")
# printing emoji that entered by user

print("Output:", emoji.emojize(emo, language='alias'))
