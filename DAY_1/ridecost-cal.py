#Ride Cost Calculator
travelling_km=int(input("Enterdistance travelled->"))
fuel_cost=int(input("Enter the cost of fule->"))
vehicle_fuel_avg=int(input("Enter average ->"))
fuel_consumption = (travelling_km / vehicle_fuel_avg)
cost_per_day = (fuel_cost * fuel_consumption)
print("Fule consumption->",fuel_consumption,"\nCost for a day->",cost_per_day)