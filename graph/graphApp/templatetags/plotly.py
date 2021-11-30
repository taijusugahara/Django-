from django import template
#plotlyをinstalled_appに入れた
import plotly.graph_objects as go
register = template.Library()

@register.simple_tag
def plotly(l1,l2):
  fig = go.Figure(
        go.Scatter(x=l1, y=l2,
        # layout=go.Layout(width=500, height=400)
    ))
  fig.update_layout(
    margin=dict(l=20,r=20,t=20,b=20)
  )
  
  return fig.to_html(fig)
