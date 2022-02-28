import carClass as C
import CustomerClass as cc
import ServiceQuoteclass as s 

Mazda=C.Car('Mazda','3 Hatchback','2020')
print('Intital Results:',Mazda.get_make(),Mazda.get_model(),Mazda.get_year())


Mazda.set_make('Tesla')
Mazda.set_year('2022')
Mazda.set_model("X")

print('New Results:',Mazda.get_make(),Mazda.get_model(),Mazda.get_year())


Cole=cc.Customer('Cole','909 Baylor ave','(691)878-9999')
print('Intially',Cole.get_name(),Cole.get_address(),Cole.get_phone())

Cole.set_name('Matt')
Cole.set_address('23 South 2nd street')
Cole.set_phone('(949) 466-9990')

print("New Results:",Cole.get_name(),Cole.get_address(),Cole.get_phone())

Tires=s.ServiceQuote(999,1000)
print('Initial results:',Tires.get_labor_charges(),Tires.get_parts_charges(),'$',format(Tires.get_sales_tax(),',.2f'),'$',format(Tires.get_total_charges(),',.2f'))

Tires.set_parts_charges(1200)
Tires.set_labor_charges(2000)
print('Final Results:',Tires.get_labor_charges(),Tires.get_parts_charges(),'$',format(Tires.get_sales_tax(),',.2f'),'$',format(Tires.get_total_charges(),',.2f'))

