#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
import json


report = SimpleDocTemplate("./report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# report.build([report_title])

with open('./fruit.json', 'r') as f:
    fruit = json.load(f)


table_data = []
for key, value in fruit.items():
    table_data.append([key, value])

# Table
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# Pie Chart
report_pie = Pie(width=3, height=3)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
# print(report_pie.data)
# print(report_pie.labels)
report_chart = Drawing()
report_chart.add(report_pie)

# Generate PDF
report.build([report_title, report_table, report_chart])
