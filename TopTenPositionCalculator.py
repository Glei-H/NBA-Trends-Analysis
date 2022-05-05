from openpyxl import load_workbook

SHEET_SUFFIX = "NBA"

class TopTenPositionCalculator:
  def __init__(self):
    self.workbook = load_workbook("nba-data-2005-2020.xlsx")

  def calculate(self, startYear, endYear):
    years = range(startYear, endYear + 1)
    modes = []
    for year in years:
      modes.append(self.mode(year))
    return modes

  def mode(self, year):
    sheet = self.workbook[str(year) + SHEET_SUFFIX]
    positionTotals = {}
    for i in range(2, 12):
      position = sheet["C" + str(i)].value
      if position in positionTotals:
        positionTotals[position] += 1
      else:
        positionTotals[position] = 1
    mode = None
    numMode = 0
    for position, numPosition in positionTotals.items():
      if numPosition > numMode:
        mode = position
        numMode = numPosition
    return mode