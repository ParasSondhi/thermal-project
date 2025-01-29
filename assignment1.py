#write a computer program that shall calculate efficiency and non dimensional 
# specific work output for different pressure ratio and turbine inlet temperatures 
# for a gas turbine cycle.
rp= float(input("Enter the pressure ratio: "))
t1= float(input("Enter the turbine inlet temperature in Kelvin: "))
eff=1-(1/(rp**0.2857))
print(f'The efficiency of the gas turbine cycle is : {eff*100:.2f}%')
t3=t1*(rp**0.57142857143)
t2=t1*(rp**0.2857)
t4=t3/(rp**0.2857)
wc=1.005*(t2-t1)
wt=1.005*(t3-t4)
w=wt-wc
print(f'Maximum work output : {w:.2f} KJ/Kg')
WR=1-(wc/wt)
print(f'Work ratio : {WR:.2f}')
print('Assumed values : \n Cp=1.005KJ/KgK \n Gamma=1.4')


