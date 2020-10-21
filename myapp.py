print("Title of program: Exam Prep bot")
print()
while True:
  description = input("Exams are coming, how do you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("you should take sufficient breaks and relax, some stress is good but too much is unhealthy")
      counter += 1
    if each_word == "confident":
      feelings_list.append("confident")
      encouragement_list.append("you can do it, continue working hard and you will make it")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think, take a break and continue your good work")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do know that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()

