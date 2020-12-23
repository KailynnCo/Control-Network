#You need to control the number of people who can be in your companies network. Groups of people can always leave the network, but a group cannot enter the network if they would make the number of people in the network exceed the maximum of 100 occupants. Write a program that reads the sizes of the groups that arrive or depart. Use negative numbers for departures. After each input, display the current number of occupants. As soon as the bar holds the maximum number of people, report that the network is full and exit the program.

#define total occupants first
total_occupants = 0

#use a while loop so it can keep looping the occupants
while(total_occupants < 100):
  
#group size number that come in or decide to leave
  print("Hello please enter the size of group arrive / depart : ")
  network_size = int(input())

#now i have to add the group size to the count of total occupants
  total_occupants = network_size + total_occupants

#check whether the total occupants count reached maximum
  if(total_occupants == 100): #if the total occupants equals 100 then let the user know we hit the limit

#network is full and exiting from loop
    print("Sorry the network is now full.")

  elif(total_occupants > 100): # now if its actually greater then 100. Let the user know they exceed the limit
    total_occupants = total_occupants - network_size
    print(network_size, "Networks can not be added because it will exceed network limit. Please try again") #this will let the users know why they exceeded 100. 
    break
  

#displaying total occupants currently there in the network
print("Total number of occupants in the network right now : ", total_occupants)