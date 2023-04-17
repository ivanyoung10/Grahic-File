import matplotlib.pyplot as plot
# set up your lists
numlist = [3, 5, 6, 8]
namelist = ['seniors', 'juniors', 'sophomores', 'freshmen']
colorlist = ['blue', 'orange', 'purple', 'red' ]
explodelist = [0.0, 0.1, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 75)
plot.axis('equal')
plot.savefig('piechart.png')
