import functions as f
import data as d
import analysis as a


def produce_analysis():
    print(a.string + '财务报表分析')
    print('\n')
    print('一、资产负债表分析：')
    current_asset_composition = f.component_analysis(d.ca_no+1, d.current_asset_no)
    non_current_asset_composition = f.component_analysis(d.nca_no+1, d.non_current_asset_no)
    current_liability_composition = f.component_analysis(d.cl_no+1, d.current_liability_no)
    non_current_liability_composition = f.component_analysis(
        d.ncl_no+1, d.non_current_liability_no)
    for i in range(len(d.years)):
        print('截止至' + str(d.years[i])
              + ', 项目集团总资产为'
              + str(round(d.total_asset[i], 2)) + '万元。'
              + '同比较去年变化'
              + f.total_asset_change[i] + '。 '
              + '其中，流动资产('+str(round(d.current_asset[i], 2)) + '万元)占比为' +
              str(round(
                  100*(d.current_asset[i]/d.total_asset[i]), 2)) + ' %。'
              + '非流动资产('+str(round(d.non_current_asset[i], 2)) + '万元)占比为' +
              str(round(
                  100*(d.non_current_asset[i]/d.total_asset[i]), 2)) + ' %。'
              + '流动资产的主要由'
              + current_asset_composition[i][0][0] +
              '(' + str(current_asset_composition[i][0][1]) + '万元), '
              + current_asset_composition[i][1][0] +
              '(' + str(current_asset_composition[i][1][1]) + '万元)和'
              + current_asset_composition[i][2][0] +
              '(' + str(current_asset_composition[i][2][1]) + '万元)组成。'
              + current_asset_composition[i][0][0] + '占总流动资产的' +
              current_asset_composition[i][0][2] + ', '
              + current_asset_composition[i][1][0] + '占总流动资产的' +
              current_asset_composition[i][1][2] + ', '
              + current_asset_composition[i][2][0] + '占总流动资产的' +
              current_asset_composition[i][2][2] + '。 '
              + '非流动资产的主要由'
              + non_current_asset_composition[i][0][0] +
              '(' + str(non_current_asset_composition[i][0][1]) + '万元), '
              + non_current_asset_composition[i][1][0] +
              '(' + str(non_current_asset_composition[i][1][1]) + '万元)和'
              + non_current_asset_composition[i][2][0] +
              '(' + str(non_current_asset_composition[i][2][1]) + '万元)组成。'
              + non_current_asset_composition[i][0][0] + '占总非流动资产的' +
              non_current_asset_composition[i][0][2] + ', '
              + non_current_asset_composition[i][1][0] + '占总非流动资产的' +
              non_current_asset_composition[i][1][2] + ', '
              + non_current_asset_composition[i][2][0] + '占总非流动资产的' +
              non_current_asset_composition[i][2][2] + '。 ')
        print('截止至' + str(d.years[i])
              + '项目集团总负债为'
              + str(round(d.total_liability[i], 2)) + '万元。'
              + '同比较去年变化'
              + f.total_liability_change[i] + '。 '
              + '其中，流动负债占比为' +
              str(round(
                  100*(d.current_liability[i]/d.total_liability[i]), 2)) + ' %。'
              + '非流动负债占比为' +
              str(round(
                  100*(d.non_current_liability[i]/d.total_liability[i]), 2)) + ' %。'
              + '流动负债的主要由'
              + current_liability_composition[i][0][0] +
              '(' + str(current_liability_composition[i][0][1]) + '万元), '
              + current_liability_composition[i][1][0] +
              '(' + str(current_liability_composition[i][1][1]) + '万元)和'
              + current_liability_composition[i][2][0] +
              '(' + str(current_liability_composition[i][2][1]) + '万元)组成。'
              + current_liability_composition[i][0][0] + '占总流动负债的' +
              current_liability_composition[i][0][2] + ', '
              + current_liability_composition[i][1][0] + '占总流动负债的' +
              current_liability_composition[i][1][2] + ', '
              + current_liability_composition[i][2][0] + '占总流动负债的' +
              current_liability_composition[i][2][2] + '。 '
              + '非流动负债的主要由'
              + non_current_liability_composition[i][0][0] +
              '(' + str(non_current_liability_composition[i][0][1]) + '万元), '
              + non_current_liability_composition[i][1][0] +
              '(' + str(non_current_liability_composition[i][1][1]) + '万元)和'
              + non_current_liability_composition[i][2][0] +
              '(' + str(non_current_liability_composition[i][2][1]) + '万元)组成。'
              + non_current_liability_composition[i][0][0] + '占总非流动负债的' +
              non_current_liability_composition[i][0][2] + ', '
              + non_current_liability_composition[i][1][0] + '占总非流动负债的' +
              non_current_liability_composition[i][1][2] + ', '
              + non_current_liability_composition[i][2][0] + '占总非流动负债的' +
              non_current_liability_composition[i][2][2] + '。 ')
        print('在' + str(d.years[i]) + '项目集团资产负债率为' +
              str(100*f.liability_asset_ratio[i]) + '%'
              + '同比较去年变化'
              + f.liability_asset_ratio_change[i] + '。 ')
    print('\n')

    print('二、利润表分析:')
    gross_profit = [r-o for r, o in zip(d.revenue, d.operating_expense)]
    gross_profit_ratio = f.percentageOccupied(gross_profit, d.revenue)
    gross_profit_ratio_change = f.percentageChange(f.ratio(gross_profit, d.revenue))
    period_expense = []
    for i in range(len(d.selling_expense)):
        period_expense.append(
            sum([d.selling_expense[i], d.management_expense[i], d.financing_expense[i]]))
    period_expense_ratio = f.percentageOccupied(period_expense, d.revenue)
    for i in range(len(d.years)):
        print('截止至' + str(d.years[i])
              + ', 项目集团营业收入为'
              + str(round(d.revenue[i], 2)) + '万元。'
              + '同比较去年变化'
              + f.revenue_change[i] + '。 '
              + '项目集团营业成本为'
              + str(round(d.operating_expense[i], 2)) + '万元。'
              + '同比较去年变化'
              + f.operating_expense_change[i] + '。 '
              + str(d.years[i]) + '实现净利润为'
              + str(round(d.net_profit[i], 2)) + '万元。 '
              + '同比较去年变化'
              + f.net_profit_change[i] + '。 ')
        print('截止至' + str(d.years[i])
              + ', 项目集团的的销售费用为'
              + str(round(d.selling_expense[i], 2)) + '万元。'
              + '同比较去年变化'
              + f.selling_expense_change[i] + '。 '
              + '项目集团的管理费用为'
              + str(round(d.management_expense[i], 2)) + '万元。'
              + '同比较去年变化'
              + f.management_expense_change[i] + '。 '
              + '项目集团的财务费用为'
              + str(round(d.financing_expense[i], 2)) + '万元。'
              + '同比较去年变化'
              + f.financing_expense_change[i] + '。 '
              + '三项期间费用的总和为'
              + str(round(period_expense[i], 2)) + '万元。'
              + '其在营业收入的占比为'
              + str(period_expense_ratio[i]) + '。 ')

        print('在' + str(d.years[i]) + '项目集团资毛利率为'
              + gross_profit_ratio[i]
              + '同比较去年变化'
              + gross_profit_ratio_change[i] + '。 ')
    print('\n')
    print('三、现金流量表分析:')
    for i in range(len(d.years)):
        print('在' + str(d.years[i])
              + ', 项目集团经营活动产生的现金净流量为'
              + str(round(d.operation_cashflow[i], 2)) + '万元，'
              + '同比较去年变化'
              + f.operation_cashflow_change[i] + '。 '
              + '项目集团投资活动产生的现金净流量为'
              + str(round(d.investment_cashflow[i], 2)) + '万元，'
              + '同比较去年变化'
              + f.investment_cashflow_change[i] + '。 '
              + '项目集团筹资活动产生的现金净流量为'
              + str(round(d.financing_cashflow[i], 2)) + '万元，'
              + '同比较去年变化'
              + f.financing_cashflow_change[i] + '。 ')


def perform_analysis():
    # d.loc = input("请输入财务报表的地址：")
    # start_year = input("请输入财务报表的起始年份：")
    # end_year = input("请输入财务报表的截止年份：")
    # d.years = list(range(start_year, end_year+1))
    produce_analysis()
    print('\n')
    print('\n')
    print("=======基础信息整理========")
    print('\n')
    a.asset_liability_analysis()
    a.profit_analysis()
    a.cashflow_analysis()
    a.ratio_analysis()


perform_analysis()
