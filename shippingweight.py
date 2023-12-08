weight = 41.5
#GROUND SHIPPING

if weight <= 2:
  cost_ground = weight * 1.5 + 20

elif weight <= 6:
  cost_ground = weight * 3.0 + 20

 

elif weight <= 10:
 cost_ground = weight * 4.0 + 20


else:
 cost_ground = weight * 4.75 + 20

 


#premium shipping
cost_of_premium_shipping = 125.00


#drone shipping
if weight <= 2:
  cost_of_drone = weight * 4.50 

elif weight <= 6:
  cost_of_drone = weight * 9.00

elif weight <= 10:
 cost_of_drone = weight * 12.00 


else:
 cost_of_drone = weight * 14.25 


print ("Ground Shipping $", cost_ground)
print ("Drone Shipping $", cost_of_drone )
print("Ground Shipping Premium $", cost_of_premium_shipping)
