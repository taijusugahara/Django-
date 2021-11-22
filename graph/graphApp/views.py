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