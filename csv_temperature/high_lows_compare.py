import csv
from datetime import datetime 

from matplotlib import pyplot as plt 

# Get dates, high and low temperatures from file.
#filename = 'sitka_weather_2014.csv'
filename_death = 'death_valley_2014.csv'
filename_sitka = 'sitka_weather_2014.csv'

def collect_data(filename):
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		
		dates, highs, lows = [], [], []
		for row in reader:
			try:
				current_date = datetime.strptime(row[0], "%Y-%m-%d")
				high = int(row[1])
				low = int(row[3])
			except ValueError:
				print(current_date, 'missing data')
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)
	return dates, highs, lows 

dates_death, highs_death, lows_death = collect_data(filename_death)
dates_sitka, highs_sitka, lows_sitka = collect_data(filename_sitka)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_death, highs_death, c='red', alpha=0.5)
plt.plot(dates_death, lows_death, c='blue', alpha=0.5)
plt.fill_between(dates_death, highs_death, lows_death, facecolor='blue', alpha=0.1)

plt.plot(dates_sitka, highs_sitka, c='green', alpha=0.5)
plt.plot(dates_sitka, lows_sitka, c='yellow', alpha=0.5)
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)


# Format plot.
title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
