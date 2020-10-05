import matplotlib.pyplot as plt
import io
import base64

def make_chart(x, y, param):
 
    fig, ax = plt.subplots(figsize = (8,6))
    ax.bar(x, y)
    ax.set_title('average {}'.format(param))
    img = io.BytesIO()
    fig.savefig(img, format = 'png')
    img.seek(0)
    chart = base64.b64encode(img.getvalue()).decode()
    plt.close()

    chart_url = 'data:image/png;base64,{}'.format(chart)

    return chart_url