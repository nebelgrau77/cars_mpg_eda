from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.models import ColumnDataSource, CategoricalColorMapper
from bokeh.models import HoverTool

def simple_bokeh_chart():
	'''make a simple line chart'''

	# chart defaults
	color = "#FF0000"
	start = 0
	finish = 20

	# create a line graph
	x = list(range(start, finish+1))
	fig = figure(title='Polynomial')
	fig.line(x, [i**2 for i in x], color = color, line_width = 3)

	#grab the static resources
	js_resources = INLINE.render_js()
	css_resources = INLINE.render_css()

	#get the resources from the figure components
	script, div = components(fig)

	return script, div, js_resources, css_resources

def better_bokeh_chart(data,size_coeff, chart_title):
	'''make a chart with supplied data'''

	mapper = CategoricalColorMapper(factors = ['AMERICA', 'ASIA', 'EUROPE'], palette = ['#aa0000', '#00aa00', '#0000aa'])

	# define data source
	source = ColumnDataSource(data = {'weight':[int(item[0]) for item in data], 
									'consumption':[round(item[1],1) for item in data],
									'origin':[item[3] for item in data], 
									'hp':[int(item[2]) for item in data],
									'brand':[item[4] for item in data],
									'model':[item[5] for item in data],
									'year':[int(item[6]) for item in data],
									'size':[item[2]*size_coeff for item in data],
									})

	# chart defaults
	color = "#111e6c"
	
	# define info to be shown when hovering over the points
	hover = HoverTool(tooltips = [('brand','@brand'),
								('model', '@model'),
								('year', '@year'),
								('origin', '@origin'),
								('weight [kg]', '@weight'),
								('fuel consumption [l/100km]', '@consumption'),
								('engine power [HP]', '@hp'),
								])

	# create a scatter plot	
	fig = figure(title=chart_title, tools = [hover, 'pan', 'wheel_zoom'], x_axis_label = 'weight [kg]', y_axis_label = 'fuel consumption [l/100 km]')	
	fig.scatter('weight', 'consumption', source = source, marker = "circle", color = {'field':'origin', 'transform':mapper}, size = 'size', alpha = 0.5, legend = 'origin')
	fig.legend.location = 'top_left'

	#grab the static resources
	js_resources = INLINE.render_js()
	css_resources = INLINE.render_css()

	#get the resources from the figure components
	script, div = components(fig)

	return script, div, js_resources, css_resources