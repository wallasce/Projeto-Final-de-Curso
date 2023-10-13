from django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# Create your views here.

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["1", "2", "3", "4", "5", "6", "7"]

    def get_providers(self):
        """Return names of datasets."""
        return ["SetPoint", "Temperature"]

    def get_data(self):
        """Return 2 datasets to plot."""

        return [[20, 20, 20, 20, 20, 20, 20],
                [10, 15, 16, 17, 18, 19, 20]]


lineChart = TemplateView.as_view(template_name='Charts/lineChart.html')
lineChartJson = LineChartJSONView.as_view()