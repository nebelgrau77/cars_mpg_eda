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

def multi_chart(x, y, param, unit):
	'''make a bar chart with supplied data, return a formatted URL'''
  
	fig, ax = plt.subplots(figsize = (10,6))
	ax.scatter(x, y, color = '#3C99DC')
	
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