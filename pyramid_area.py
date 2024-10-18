#Input variables
side_length = float(input("Enter the side length in meters: "))
layer_num = int(input("Enter the number of layers: "))


# initializing values
layer_start = 0
one_side_total = 0


#for loop enabling the calculation for the amount of layers
for i in range(layer_num):


   #if statement  ensuring the amount of layers is greater than 1
   if layer_num > 1:
       one_layer = layer_start + 1         # starting at the top layer
       layer_start += 1                    # moving down one layer, adding one
       one_side_total += one_layer         # making a total of all the layers
 
   #if condition holds false, run this else statement
   else:
       #assign 0 to the visible cubes per layer
       visible_cubes_per_layer = 0


#top face area calculation, the amount of layers squared times side length squared.
top_face_area = (layer_num ** 2) * (side_length ** 2)


#calculate the side faces area (four side faces times the area of each square)
side_faces_area = (one_side_total * 4) * (side_length ** 2)
 
#use top face area and side face area to calculate total area
total_area = top_face_area + side_faces_area


#final print statement
print(f'You need {total_area:.2f} m^2 of gold foil to cover the pyramid')
