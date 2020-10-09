import matplotlib.pyplot as plt
import io
import base64

def simple_chart(x, y, param, unit):
	'''make a bar chart with supplied data, return a formatted URL'''
  
	fig, ax = plt.subplots(figsize = (10,6))
	ax.bar(x, y, color = '#3C99DC')
	
	if not param:
		param = 'weight'
	
	if not unit:
		unit = 'kg'
	
	ax.set_title('Average {} kg'.format(param))
	ax.set_title('Average {}'.format(param))
	ax.set_xticks(x)
	ax.set_xlabel('Model year')
	ax.set_ylabel('{} [{}]'.format(param.title(), unit))
	img = io.BytesIO()
	fig.savefig(img, format = 'png')
	img.seek(0)
	chart = base64.b64encode(img.getvalue()).decode()
	plt.close()

	chart_url = 'data:image/png;base64,{}'.format(chart)

	return chart_url

def multi_chart(x, y, param1, param2, size, category, unit1, unit2): 
	'''make a bar chart with supplied data, return a formatted URL'''
  
	fig, ax = plt.subplots(figsize = (10,6))
	ax.scatter(x, y, s = size, color = '#3C99DC', alpha = 0.3)
	
	if not param1:
		param1 = 'horsepower'
		unit1 = 'HP'
		param2 = 'weight'	
		unit1 = 'kg'
	
	#ax.set_title('Average {}'.format(param))
	ax.set_xticks(x)
	ax.set_xlabel('{} [{}]'.format(param1.title(), unit1))
	ax.set_ylabel('{} [{}]'.format(param2.title(), unit2))
	img = io.BytesIO()
	fig.savefig(img, format = 'png')
	img.seek(0)
	chart = base64.b64encode(img.getvalue()).decode()
	plt.close()

	chart_url = 'data:image/png;base64,{}'.format(chart)

	return chart_url

def colored_chart(queries, categories, params, units):
	
	fig, ax = plt.subplots(figsize = (10,6))

	colors = ['r', 'g', 'b']

	size_coeff = 0.5

	for query, color in zip(queries, colors):
		x = [item[0] for item in query]
		y = [item[1] for item in query]
		size = [item[2] * size_coeff for item in query]

		scatter = ax.scatter(x,y,s=size, c=color, alpha=0.3)


	# produce a legend with the unique colors from the scatter
	

	ax.legend(categories)

	ax.set_title('point size: {}'.format(params[2]))
	ax.set_xlabel('{} [{}]'.format(params[0], units[0]))
	ax.set_ylabel('{} [{}]'.format(params[1], units[1]))

	#ax.set_xlim(left=0)
	ax.set_ylim(bottom=0)

	img = io.BytesIO()
	fig.savefig(img, format = 'png')
	img.seek(0)
	chart = base64.b64encode(img.getvalue()).decode()
	plt.close()

	chart_url = 'data:image/png;base64,{}'.format(chart)

	return chart_url

	
def better_colored_chart(query):
	
	fig, ax = plt.subplots(figsize = (10,6))

	colors = ['r', 'g', 'b']	

	size_coeff = 0.5

	x = [item[0] for item in query]
	y = [item[1] for item in query]
	size = [item[2] * size_coeff for item in query]
	categories = [item[3] for item in query]
	
	cats = list(set(categories))

	colorcats = {cat:color for cat, color in zip(cats, colors)}

	ax.scatter(x,y,s=size, c=[colorcats[cat] for cat in categories], alpha=0.3)

	#legend1 = ax.legend(*scatter.legend_elements(),loc="lower left", title="Categories")
	#ax.add_artist(legend1)

	#ax.set_title('point size: {}'.format(params[2]))
	#ax.set_xlabel('{} [{}]'.format(params[0], units[0]))
	#ax.set_ylabel('{} [{}]'.format(params[1], units[1]))

	#ax.set_xlim(left=0)
	ax.set_ylim(bottom=0)

	img = io.BytesIO()
	fig.savefig(img, format = 'png')
	img.seek(0)
	chart = base64.b64encode(img.getvalue()).decode()
	plt.close()

	chart_url = 'data:image/png;base64,{}'.format(chart)

	return chart_url