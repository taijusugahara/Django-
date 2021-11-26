from django.shortcuts import render

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import xml.etree.cElementTree as ET
# Create your views here.

def index(request):
  tree = ET.parse('tera.xml')
  root = tree.getroot()

  l = []
  for value in root.iter('machine1'):
    l.append(float(value.text))
  plt.plot(l,color="navy")
  plt.savefig('static/img/graph/machine1_graph.png')

  l2 =[]
  for value in root.iter('machine2'):
    l2.append(float(value.text))
  plt.figure()
  plt.plot(l2,color="navy")
  plt.savefig('static/img/graph/machine2_graph.png')

  l3 =[]
  for value in root.iter('machine3'):
    l3.append(float(value.text))
  plt.figure()
  plt.plot(l3,color="navy")
  plt.savefig('static/img/graph/machine3_graph.png')

  return render(request,'index.html')


def CustomTemplateTag(request):
  return render(request,'customtag.html',context={
    'l1' : [1,2,3,4,5],
    'l2' : [10,9,8,7,6]
  })


def PlotlyGraph(request):
  tree = ET.parse('tera.xml')
  root = tree.getroot()
  l = []
  for value in root.iter('machine1'):
    l.append(float(value.text))
  l2 =[]
  for value in root.iter('machine2'):
    l2.append(float(value.text))
  l3 =[]
  for value in root.iter('machine3'):
    l3.append(float(value.text))

  array_list =[l,l3]

  return render(request,'plotly_graph.html',context={
    'list' : array_list,
    'l2' : l2
  })