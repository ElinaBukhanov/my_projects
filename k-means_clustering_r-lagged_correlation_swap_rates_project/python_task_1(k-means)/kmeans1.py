#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
k means a
"""

##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Sun Mar  1 18:44:47 2020
#
#@author: elina
#"""
#question 1 a
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#reading data
afi = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/afi.csv", skiprows=2 )
airportcity = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/airportcity.csv", skiprows=2 )
alony = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/alony.csv", skiprows=2 )
amot = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/amot.csv", skiprows=2 )
azrieli = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/azrieli.csv", skiprows=2 )
bayside = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/bayside.csv", skiprows=2 )
bazan = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/bazan.csv", skiprows=2 )
bezeq = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/bezeq.csv", skiprows=2 )
big = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/big.csv", skiprows=2 )
clal_insurance = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/clal_insurance.csv", skiprows=2 )
compugen = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/compugen.csv", skiprows=2 )
delek_drill_l = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/delek_drill_l.csv", skiprows=2 )
delek_group = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/delek_group.csv", skiprows=2 )
discount = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/discount.csv", skiprows=2 )
elbit = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/elbit.csv", skiprows=2 )
electra = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/electra.csv", skiprows=2 )
energix = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/energix.csv", skiprows=2 )
enlight_energy = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/enlight_energy.csv", skiprows=2 )
equital = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/equital.csv", skiprows=2 )
fibi = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/fibi.csv", skiprows=2 )
fibi_holdings = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/fibi_holdings.csv", skiprows=2 )
formula = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/formula.csv", skiprows=2 )
gazit = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/gazit.csv", skiprows=2 )
hapoalim = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/hapoalim.csv", skiprows=2 )
harel = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/harel.csv", skiprows=2 )
hilan = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/hilan.csv", skiprows=2 )
icl = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/icl.csv", skiprows=2 )
indus = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/indus.csv", skiprows=2 )
israel_corp = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/israel_corp.csv", skiprows=2 )
isramco = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/isramco.csv", skiprows=2 )
leumi = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/leumi.csv", skiprows=2 )
lvpsn = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/lvpsn.csv", skiprows=2 )
matrix = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/matrix.csv", skiprows=2 )
mega_or = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/mega_or.csv", skiprows=2 )
melisron = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/melisron.csv", skiprows=2 )
mizrahi = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/mizrahi.csv", skiprows=2 )
nice = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/nice.csv", skiprows=2 )
nova = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/nova.csv", skiprows=2 )
partner = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/partner.csv", skiprows=2 )
paz = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/paz.csv", skiprows=2 )
phoenix = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/phoenix.csv", skiprows=2 )
reit1 = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/reit1.csv", skiprows=2 )
sapiens = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/sapiens.csv", skiprows=2 )
sella = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/sella.csv", skiprows=2 )
shikun = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/shikun.csv", skiprows=2 )
shufersal = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/shufersal.csv", skiprows=2 )
strauss = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/strauss.csv", skiprows=2 )
summit = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/summit.csv", skiprows=2 )
teva = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/teva.csv", skiprows=2 )
tower = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/tower.csv", skiprows=2 )


#functions for calculating mean and variance
def data_ret_mean(df):
    df['Date'] =pd.to_datetime(df.Date)
    df.sort_values(by=['Date'], inplace=True, ascending=True)
    df = df.set_index(['Date'])
    df_returns = df['Adjusted Closing Price'].pct_change().mean()
    return df_returns
    
def data_ret_var(df):
    df['Date'] =pd.to_datetime(df.Date)
    df.sort_values(by=['Date'], inplace=True, ascending=True)
    df = df.set_index(['Date']) 
    df_variance = df['Adjusted Closing Price'].pct_change().std()
    return df_variance


afi_returns = data_ret_mean(afi)
afi_variance = data_ret_var(afi)

airportcity_returns = data_ret_mean(airportcity)
airportcity_variance = data_ret_var(airportcity)

alony_returns = data_ret_mean(alony)
alony_variance = data_ret_var(alony)

amot_returns = data_ret_mean(amot)
amot_variance =  data_ret_var(amot)

azrieli_returns = data_ret_mean(azrieli)
azrieli_variance = data_ret_var(azrieli)

bayside_returns = data_ret_mean(bayside)
bayside_variance = data_ret_var(bayside)

bazan_returns = data_ret_mean(bazan)
bazan_variance = data_ret_var(bazan)

bezeq_returns = data_ret_mean(bezeq)
bezeq_variance = data_ret_var(bezeq)

big_returns = data_ret_mean(big)
big_variance = data_ret_var(big)

clal_insurance_returns = data_ret_mean(clal_insurance)
clal_insurance_variance = data_ret_var(clal_insurance)

compugen_returns = data_ret_mean(compugen)
compugen_variance = data_ret_var(compugen)

delek_drill_l_returns = data_ret_mean(delek_drill_l)
delek_drill_l_variance = data_ret_var(delek_drill_l)

delek_group_returns = data_ret_mean(delek_group)
delek_group_variance = data_ret_var(delek_group)

discount_returns = data_ret_mean(discount)
discount_variance = data_ret_var(discount)

elbit_returns = data_ret_mean(elbit)
elbit_variance = data_ret_var(elbit)

electra_returns = data_ret_mean(electra)
electra_variance = data_ret_var(electra)

energix_returns = data_ret_mean(energix)
energix_variance = data_ret_var(energix)

enlight_energy_returns = data_ret_mean(enlight_energy)
enlight_energy_variance = data_ret_var(enlight_energy)

equital_returns = data_ret_mean(equital)
equital_variance = data_ret_var(equital)

fibi_returns = data_ret_mean(fibi)
fibi_variance = data_ret_var(fibi)

fibi_holdings_returns = data_ret_mean(fibi_holdings)
fibi_holdings_variance = data_ret_var(fibi_holdings)

formula_returns = data_ret_mean(formula)
formula_variance = data_ret_var(formula)

gazit_returns = data_ret_mean(gazit)
gazit_variance = data_ret_var(gazit)

hapoalim_returns = data_ret_mean(hapoalim)
hapoalim_variance = data_ret_var(hapoalim)

harel_returns = data_ret_mean(harel)
harel_variance = data_ret_var(harel)

hilan_returns = data_ret_mean(hilan)
hilan_variance = data_ret_var(hilan)

icl_returns = data_ret_mean(icl)
icl_variance = data_ret_var(icl)

indus_returns = data_ret_mean(indus)
indus_variance = data_ret_var(indus)

israel_corp_returns = data_ret_mean(israel_corp)
israel_corp_variance = data_ret_var(israel_corp)

isramco_returns = data_ret_mean(isramco)
isramco_variance = data_ret_var(isramco)

leumi_returns = data_ret_mean(leumi)
leumi_variance = data_ret_var(leumi)

lvpsn_returns = data_ret_mean(lvpsn)
lvpsn_variance = data_ret_var(lvpsn)

matrix_returns = data_ret_mean(matrix)
matrix_variance = data_ret_var(matrix)

mega_or_returns = data_ret_mean(mega_or)
mega_or_variance = data_ret_var(mega_or)

melisron_returns = data_ret_mean(melisron)
melisron_variance = data_ret_var(melisron)

mizrahi_returns = data_ret_mean(mizrahi)
mizrahi_variance = data_ret_var(mizrahi)

nice_returns = data_ret_mean(nice)
nice_variance = data_ret_var(nice)

nova_returns = data_ret_mean(nova)
nova_variance = data_ret_var(nova)

partner_returns = data_ret_mean(partner)
partner_variance = data_ret_var(partner)

paz_returns = data_ret_mean(paz)
paz_variance = data_ret_var(paz)

phoenix_returns = data_ret_mean(phoenix)
phoenix_variance = data_ret_var(phoenix)

reit1_returns = data_ret_mean(reit1)
reit1_variance = data_ret_var(reit1)

sapiens_returns = data_ret_mean(sapiens)
sapiens_variance = data_ret_var(sapiens)

sella_returns = data_ret_mean(sella)
sella_variance = data_ret_var(sella)

shikun_returns = data_ret_mean(shikun)
shikun_variance = data_ret_var(shikun)

shufersal_returns = data_ret_mean(shufersal)
shufersal_variance = data_ret_var(shufersal)

strauss_returns = data_ret_mean(strauss)
strauss_variance = data_ret_var(strauss)

summit_returns = data_ret_mean(summit)
summit_variance = data_ret_var(summit)

teva_returns = data_ret_mean(teva)
teva_variance = data_ret_var(teva)

tower_returns = data_ret_mean(tower)
tower_variance = data_ret_var(tower)

#companies
company = ['afi', 'airportcity','alony','amot','azrieli','bayside','bazan','bezeq','big','clal_insurance','compugen','delek_drill_l','delek_group','discount','elbit','electra','energix','enlight_energy','equital','fibi','fibi_holdings','formula','gazit','hapoalim','harel','hilan','icl','indus','israel_corp','isramco','leumi','lvpsn','matrix','mega_or','melisron','mizrahi','nice','nova','partner','paz','phoenix','reit1','sapiens','sella','shikun','shufersal','strauss','summit','teva','tower']

#concatenating the returns and variances into a single data-frame
data = [[afi_returns,afi_variance],[airportcity_returns,airportcity_variance],[alony_returns,alony_variance],[amot_returns,amot_variance],[azrieli_returns,azrieli_variance],[bayside_returns,bayside_variance],[bazan_returns,bazan_variance],[bezeq_returns,bezeq_variance],[big_returns,big_variance],[clal_insurance_returns,clal_insurance_variance],[compugen_returns,compugen_variance],[delek_drill_l_returns,delek_drill_l_variance], [delek_group_returns,delek_group_variance], [discount_returns,discount_variance],[elbit_returns,elbit_variance],[electra_returns,electra_variance],[energix_returns,energix_variance],[enlight_energy_returns,enlight_energy_variance],[equital_returns,equital_variance],[fibi_returns,fibi_variance],[fibi_holdings_returns,fibi_holdings_variance],[formula_returns,formula_variance],[gazit_returns,gazit_variance],[hapoalim_returns,hapoalim_variance],[harel_returns,harel_variance],[hilan_returns,hilan_variance],[icl_returns,icl_variance],[indus_returns,indus_variance],[israel_corp_returns,israel_corp_variance],[isramco_returns,isramco_variance],[leumi_returns,leumi_variance],[lvpsn_returns,lvpsn_variance],[matrix_returns,matrix_variance],[mega_or_returns,mega_or_variance], [melisron_returns,melisron_variance],[mizrahi_returns,mizrahi_variance],[nice_returns,nice_variance],[nova_returns,nova_variance],[partner_returns,partner_variance],[paz_returns,paz_variance],[phoenix_returns,phoenix_variance],[reit1_returns,reit1_variance],[sapiens_returns,sapiens_variance],[sella_returns,sella_variance],[shikun_returns,shikun_variance],[shufersal_returns,shufersal_variance],[strauss_returns,strauss_variance],[summit_returns,summit_variance],[teva_returns,teva_variance],[tower_returns,tower_variance]]
ret_var = pd.DataFrame(data, columns = ['Returns', 'Variance'])
ret_var.insert(0, 'Company', company, True)
ret_var.set_index('Company', inplace=True, drop=True)
print(ret_var.head())

#k-means
X = ret_var.values
kmeans = KMeans(n_clusters = 5).fit(X)
centroids = kmeans.cluster_centers_
plt.scatter(X[:,0],X[:,1], c = kmeans.labels_, cmap ="rainbow")
plt.show()

#getting the cluster number of each company
Company = pd.DataFrame(ret_var.index)
cluster_labels = pd.DataFrame(kmeans.labels_)
df = pd.concat([Company, cluster_labels],axis = 1)
print(df.head(50))
df.to_excel("output1a.xlsx") 
