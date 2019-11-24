import xlrd


# loc = ''
# years = []

loc = '/Users/chunyuema/Desktop/CAREER/CS/project/fam/fam.xlsx'
years = [2016, 2017, 2018, 2019]
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(1)


def get_row_number(sheet, str):
    for i in range(sheet.nrows):
        if sheet.row_values(i)[0] == str:
            return i


ca_no = get_row_number(sheet, "流动资产：")
current_asset_no = get_row_number(sheet, "流动资产合计")
current_asset = sheet.row_values(current_asset_no, 1)
funds_no = get_row_number(sheet, "货币资金")
funds = sheet.row_values(funds_no, 1)
inventory_no = get_row_number(sheet, "存货")
inventory = sheet.row_values(inventory_no, 1)
one_year_nca_no = get_row_number(sheet, "一年内到期的非流动资产")
one_year_nca = sheet.row_values(one_year_nca_no, 1)
other_ca_no = get_row_number(sheet, "其他流动资产")
other_ca = sheet.row_values(other_ca_no, 1)
quick_asset = [a - b - c - d for a, b, c,
               d in zip(current_asset, inventory, one_year_nca, other_ca)]
nca_no = get_row_number(sheet, "非流动资产：")
non_current_asset_no = get_row_number(sheet, "非流动资产合计")
non_current_asset = sheet.row_values(non_current_asset_no, 1)
total_asset_no = get_row_number(sheet, "资产总计")
total_asset = sheet.row_values(total_asset_no, 1)
cl_no = get_row_number(sheet, "流动负债：")
current_liability_no = get_row_number(sheet, "流动负债合计")
current_liability = sheet.row_values(current_liability_no, 1)
ncl_no = get_row_number(sheet, "非流动负债：")
non_current_liability_no = get_row_number(sheet, "非流动负债合计")
non_current_liability = sheet.row_values(non_current_liability_no, 1)
total_liability_no = get_row_number(sheet, "负债合计")
total_liability = sheet.row_values(total_liability_no, 1)
owner_equity_no = get_row_number(sheet, "所有者权益合计")
owner_equity = sheet.row_values(owner_equity_no, 1)


revenue_no = get_row_number(sheet, "一、营业收入")
revenue = sheet.row_values(revenue_no, 1)
operating_expense_no = get_row_number(sheet, "营业成本")
operating_expense = sheet.row_values(operating_expense_no, 1)
operating_profit_no = get_row_number(sheet, "二、营业利润")
operating_profit = sheet.row_values(operating_profit_no, 1)
selling_expense_no = get_row_number(sheet, "销售费用")
selling_expense = sheet.row_values(selling_expense_no, 1)
management_expense_no = get_row_number(sheet, "管理费用")
management_expense = sheet.row_values(management_expense_no, 1)
financing_expense_no = get_row_number(sheet, "财务费用")
financing_expense = sheet.row_values(financing_expense_no, 1)
overall_profit_no = get_row_number(sheet, "三、利润总额")
overall_profit = sheet.row_values(overall_profit_no, 1)
net_profit_no = get_row_number(sheet, "四、净利润")
net_profit = sheet.row_values(net_profit_no, 1)


operation_cashflow_no = get_row_number(sheet, "经营活动产生的现金流量净额")
operation_cashflow = sheet.row_values(operation_cashflow_no, 1)
investment_cashflow_no = get_row_number(sheet, "投资活动产生的现金流量净额")
investment_cashflow = sheet.row_values(investment_cashflow_no, 1)
financing_cashflow_no = get_row_number(sheet, "筹资活动产生的现金流量净额")
financing_cashflow = sheet.row_values(financing_cashflow_no, 1)

operation_inflow_no = get_row_number(sheet, "销售商品、提供劳务收到的现金")
operation_inflow = sheet.row_values(operation_inflow_no, 1)
operation_outflow_no = get_row_number(sheet, "购买商品、接受劳务支付的现金")
operation_outflow = sheet.row_values(operation_outflow_no, 1)

operation_ttinflow_no = get_row_number(sheet, "经营活动现金流入小计")
operation_ttinflow = sheet.row_values(operation_ttinflow_no, 1)
investment_ttinflow_no = get_row_number(sheet, "投资活动现金流入小计")
investment_ttinflow = sheet.row_values(investment_ttinflow_no, 1)
financing_ttinflow_no = get_row_number(sheet, "筹资活动现金流入小计")
financing_ttinflow = sheet.row_values(financing_ttinflow_no, 1)

operation_ttoutflow_no = get_row_number(sheet, "经营活动现金流出小计")
operation_ttoutflow = sheet.row_values(operation_ttoutflow_no, 1)
investment_ttoutflow_no = get_row_number(sheet, "投资活动现金流出小计")
investment_ttoutflow = sheet.row_values(investment_ttoutflow_no, 1)
financing_ttoutflow_no = get_row_number(sheet, "筹资活动现金流出小计")
financing_ttoutflow = sheet.row_values(financing_ttoutflow_no, 1)

total_cashflow_no = get_row_number(sheet, "五、现金及现金等价物净增加额")
total_cashflow = sheet.row_values(total_cashflow_no, 1)
