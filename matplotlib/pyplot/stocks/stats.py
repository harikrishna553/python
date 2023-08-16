import matplotlib.pyplot as plt

# From May 2023
nasdaq_index = [9.3, 10.34, 10.81, 11.03]
quant_small = [150.7, 164.26, 172.96, 185.29]
mirae_ai_fund = [11.34, 12.87, 13.53, 13.92]
sbi_contra = [236.75, 243.92, 257.19, 266.55]
motilal_midcap = [51.57, 56.46, 58.14, 59.56]
# nippon_innovation_fund = [10, 10, 10, 10]

x = [25, 50, 75,100]
xticks = list(range(0,200, 5))
yticks = list(range(0,400,15))

plt.plot(x, nasdaq_index, label = 'nasdaq_index')
plt.plot(x, quant_small, label = 'quant_small')
plt.plot(x, mirae_ai_fund, label = 'mirae_ai_fund')
plt.plot(x, sbi_contra, label = 'sbi_contra')
plt.plot(x, motilal_midcap, label = 'motilal_midcap')
# plt.plot(x, nippon_innovation_fund, label = 'nippon_innovation_fund')

plt.xticks(xticks)
plt.yticks(yticks)
plt.legend()

plt.show()