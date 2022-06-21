weight = float(input("Enter a weight: "))
weight_ground_shipping = weight
cost_ground_premium = 125.00
weight_drone_shipping = weight

#Ground Shipping

if weight_ground_shipping <= 2:
  cost_ground = 1.50 * weight_ground_shipping + 20.00
elif weight_ground_shipping > 2 and weight_ground_shipping <=6:
  cost_ground = 3.00 * weight_ground_shipping + 20.00
elif weight_ground_shipping > 6 and weight_ground_shipping <=10:
  cost_ground = 4.00 * weight_ground_shipping + 20.00
elif weight_ground_shipping > 10:
  cost_ground = 4.75 * weight_ground_shipping + 20.00

print("Cost of Ground Shipping: " + str(cost_ground))

#Ground Shipping Premium


print("Cost of Ground Shipping Premium: " + str(cost_ground_premium))

#Drone shipping


if weight_drone_shipping <= 2:
  cost_drone = 4.50 * weight_drone_shipping
elif weight_drone_shipping > 2 and weight_drone_shipping <=6:
  cost_drone = 9.00 * weight_drone_shipping
elif weight_drone_shipping > 6 and weight_drone_shipping <=10:
  cost_drone = 12.00 * weight_drone_shipping
elif weight_drone_shipping > 10:
  cost_drone = 14.25 * weight_drone_shipping

print("Cost of Drone Shipping: " + str(cost_drone))

if cost_ground < cost_ground_premium and cost_drone:
  print("\nThe cheapest option is " + "Ground Shipping, which is " + str(cost_ground))
if cost_ground_premium < cost_ground and cost_drone:
  print("\nThe cheapest option is " + "Ground Shipping Premium, which is " + str(cost_ground_premium))
if cost_drone < cost_ground and cost_ground_premium:
  print("\nThe cheapest option is " + "Drone shipping Shipping, which is " + str(cost_drone))
