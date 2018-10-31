from datetime import date
import matplotlib.pyplot as plt

def construct_dict():
	infile = open('city_temp/citylistWorld.htm','r')
	city_file_link = {}

	ptrn1 = '<li class=MsoNormal style=\'mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;'
	ptrn2 = 'mso-list:l6 level1 lfo3;tab-stops:list .5in\'><b>'
	ptrn3 = 'href=\"ftp://ftp.engr.udayton.edu/jkissock/gsod/'

	for line in infile:
		if ptrn1 not in line: continue
		line = infile.next()
		try:
			name_raw = line.split('<b>')[1].split('<')[0].split()
			if '(' in name_raw[-1] or len(name_raw) == 1:
				name = name_raw[0]
			else:
				name = name_raw[0] + ' ' + name_raw[1]
		except IndexError: print 'Failed to retrieve name: ', line
		while ptrn3 not in line: line = infile.next()
		try: file = line.split('/gsod/')[1].split('\">')[0]
		except IndexError: print 'Failed to retrieve file: ', line
		city_file_link[name] = file

	infile.close()
	return city_file_link

def read_from_city(dict,city):
	dir = 'city_temp/'
	infile = open(dir + dict[city], 'r')

	data = {}
	for line in infile:
		value = line.split()
		if value[-1] == '-99': continue
		date_ = date(eval(value[2]), eval(value[0]), eval(value[1]))
		data[date_] = float(value[-1])
		#except: print value
	infile.close()
	return data

def plot_temperatures(dict, cities, period):
	plt.xlim(period[0],period[1])
	for city in cities:
		data = read_from_city(dict,city)
		plt.plot(sorted(data), [data[d] for d in data], label=city)
	plt.legend()
	plt.show()

city_file_link = construct_dict()
for name in city_file_link:
	print name, city_file_link[name]

dict = read_from_city(city_file_link,'Oslo')
for d in sorted(dict):
	print d, dict[d]

#plt.plot(sorted(dict), [dict[d] for d in sorted(dict)])
#plt.show()
plot_temperatures(city_file_link, ['Oslo', 'Taipei'], [date(2000,1,1),date(2000,2,1)])
