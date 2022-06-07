"""
Created on Mon Jun  6 10:47:37 2022
@author: Oscar and Johanne
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#%% Heat Demand Data

# Heat demand
Q = 56000 #Annual heat demand [MWh] 
Qbase = Q*0.3 #Base heat demand [MWh]
Qload = Q*0.7 #Temperature dependent heat load [MWh]

# Load ambient air data
Ta_data = pd.read_excel(r'Ambient air temperature 2019.xlsx') #Ambient air temperature data
Ta = Ta_data['°C'].to_numpy() #Ambient air temperature [°C]
time = np.arange(0,8760)

# Degree hours
Tset = 18 #[C]
dh = np.maximum(Tset-Ta,0) #Degree hours
sum_dh = sum(dh) #Sum of degree hours

# Hourly heating distribution
hr_sh = dh/sum_dh * Qload

# Total heat demand
HD = Qbase/(365*24) + hr_sh
HD_peak = np.max(HD)

# Plot demand
plt.plot(time,HD,Linewidth = 0.5)
plt.grid('minor')
plt.xlabel('Time [hr]')
plt.ylabel('Heat Demand [MWh]')
plt.xlim([time[0],time[-1]]) # first: [0] last: [-1]
plt.ylim([2,14])


#%% Heat Production Data

# Efficiencies
eta_CHP_el = 0.3
eta_CHP_heat = 0.75
COP_HP = 3
eta_PB = 0.95

# Capacities
Q_CHP = 0.3*HD_peak #[MW]
Q_HP = 0.3*HD_peak #[MW]
Q_PB = 0.4*HD_peak #[MW]
E_WH = 0.2*Q #[MWh]

# Cost of maintenance
gj2mwh = 3.6 #[GJ/MWh]
cm_CHP = 5*gj2mwh #Maintenance cost CHP [DKK/MWh]
cm_HP = 2*gj2mwh #Maintenance cost HP [DKK/MWh]
cm_PB = 1*gj2mwh #Maintenance cost PB [DKK/MWh]

# Cost of fuel
c_el = np.loadtxt('Nordpool Electricity market price 2019 DK.txt',skiprows=1) #Cost of electricity
c_bio = 45*gj2mwh #Cost of biofuel
c_ng = 50*gj2mwh #Cost of natural gas
c_wh = 10*gj2mwh #Cost of waste heat



