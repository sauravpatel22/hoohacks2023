f = open('C:\\Users\\shail\\Downloads\\user.txt', 'r')
array = f.read()
array = list(array)
results_list = []

# solar
if array[0] == 2:
   if array[1] == 4:
       if array[2] == 1 or 2:
           if array[3] == 1 or 2:
               if array[4] == 2 or 3 or 4 or 5 or 6:
                   results_list.append("You could install rooftop solar panels. While expensive, rooftop solar can reduce dependency of fossil fuels by providing electricity from the panels. It can also save money in the long run, as the amount you will need to pay for electricity will be significantly lower. Check with a consultant to determine if rooftop solar is right for your house. If you are in an area with a homeowners association, check with their guidelines as well.")

# appliances
if array[0] == 2:
   if array[1] == 3 or 4:
       if array[2] == 1 or 2:
           if array[3] == 2:
               if array[4] == 1 or 2 or 3 or 4 or 5 or 6:
                   results_list.append("Appliances:\nYou could replace your old appliances. Old appliances such as refrigerators, dishwashers. washers, and dryers are significantly less efficient than newer appliances. This can result in more electricity usage and more money spent on electricity. Replacing appliances after they have run through their effective lifetime is a great way to save money and lower energy usage.\n\n")

# Switch to LED light bulbs
results_list.append("Light Bulbs:\nYou could replace incandescent light bulbs with LEDs. While simple, this can reduce energy consumption. LED light bulbs are more efficient than incandescents and last longer, making them less expensive to maintain as well. This can be done with any type of housing and is inexpensive, quick, and easy.\n\n")

# weatherstripping windows
if array[0] == 1 or 2:
   if array[1] == 1 or 2 or 3 or 4:
       if array[2] == 2:
           if array[3] == 1 or 2:
               if array[4] == 1 or 2 or 3 or 4 or 5 or 6:
                   results_list.append("Windows:\nYou could weatherstrip your windows. Heat can escape through gaps in windows and use more energy. This problem gets worse as windows get older. Weatherstripping windows can reduce loss of electricity and reduce energy consumption.\n\n")

# cleaning fridge coils
results_list.append("Fridge:\nYou could clean the coils on your refrigerator. Refrigerator coils tend become less efficient at cooling when they are dirt. Cleaning them on a semi-regular basis can improve fridge efficiency and lower energy usage.\n\n")

# changing washing/drying cycles
results_list.append("Clothes:\nYou could lower the temperature when washing and drying clothes. Washing your clothes with cold water and using a low heat or no heat drying cycle can reduce energy usage and save money.\n\n")

# new insulation
if array[0] == 2:
   if array[1] == 4:
       if array[2] == 2:
           if array[3] == 1 or 2:
               if array[4] == 2 or 3 or 4 or 5 or 6:
                   results_list.append("Insulation:\nYou could replace old insulation. Older insulation is not able to retain heat as well, resulting in the loss of heat and the usage of more electricity. Replacing old insulation can reduce energy usage.\n\n")

# home composting
results_list.append("Compost:\nYou could start a home composting bin. This would ensure that your excess food does not go to waste and can be used. Compost also serves as a fertilizer and can be used to help grow plants.\n\n")

# heavy curtains
results_list.append("Curtains:\nYou could use heavy, heat-blocking curtains. Heat can escape through windows in the winter, resulting in higher energy usage to maintain a comfortable temperature. Heavy, heat-blocking curtains can help retain some of the heat at night, keeping energy cost and usage from heating down.\n\n")

# smart thermostat
if array[0] == 2:
   if array[1] == 2 or 3 or 4:
       if array[2] == 1 or 2:
           if array[3] == 1 or 2:
               if array[4] == 1 or 2 or 3 or 4 or 5 or 6:
                   results_list.append("Thermostat:\nYou could install a smart thermostat. You can maintain a comfortable temperature while not using more energy than necessary as it automatically adjusts temperature and the set temperature can be changed.\n\n")

# smart power strip
results_list.append("Power Strips:\nYou could use smart power strips in areas with multiple appliances plugged in. Smart power strips automatically shut off when energy is not being used which reduces energy usage from appliances that are plugged in but not on.\n\n")

# water filter
results_list.append("Water Filter:\nYou could install a water filter on your sink. This not only reduces the need for plastic water bottles and it also ensures that water is clean for cooking and drinking.\n\n")

# laundry microplastic filter
results_list.append("Microplastic Filter:\nYou could install a microplastic filter on your washer. Microplastics tend to shed off of clothing during wash cycles. A microplastic filter can help capture these microplastics and prevent them from ending up in waterways.\n\n")

with open("C:\\Users\\shail\\Downloads\\user2.txt", 'w') as f:
   for result in results_list:
       f.write(result)
       f.write("\n")

f.close()
