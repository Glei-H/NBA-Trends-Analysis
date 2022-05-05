from openpyxl import load_workbook

SHEET_SUFFIX = "NBA"

class ThreePointCalculator:
  def __init__(self):
    self.workbook = load_workbook("nba-data-2005-2020.xlsx")
  
  def calculate(self, startYear, endYear):
    years = range(startYear, endYear + 1)
    averages = []
    for year in years:
      averages.append(self.average(year))
    return averages

  def average(self, year):
    sheet = self.workbook[str(year) + SHEET_SUFFIX]
    sum = 0
    for i in range(2, 12):
      sum += sheet["L" + str(i)].value
    return sum / 10