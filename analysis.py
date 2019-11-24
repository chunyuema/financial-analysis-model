import data as d
import functions as f
string = str(d.years[0]) + '--' + str(d.years[len(d.years)-1])


def asset_liability_analysis():
    print("一、资产负债表分析:")
    print("1. 基本信息：")
    print(string + '总资产:', [round(i, 2) for i in d.total_asset])
    print(string + '总资产变化率:', f.total_asset_change)
    print(string + '总负债:', [round(i, 2) for i in d.total_liability])
    print(string + '总负债变化率:', f.total_liability_change)
    print("1. 流动非流动资产组成分析:")
    print('a.'+string + "流动资产占比：", f.percentageOccupied(d.current_asset, d.total_asset))
    print('b.'+string + "非流动资产占比：", f.percentageOccupied(d.non_current_asset, d.total_asset))
    print('c.'+string + "流动资产主要组成分析:")
    current_asset_composition = f.component_analysis(d.ca_no+1, d.current_asset_no)
    for i in range(len(d.years)):
        print(str(d.years[i]), current_asset_composition[i])
    print('d.'+string + "非流动资产主要组成分析(前三项):")
    non_current_asset_composition = f.component_analysis(d.nca_no+1, d.non_current_asset_no)
    for i in range(len(d.years)):
        print(str(d.years[i]), non_current_asset_composition[i])
    print("2. 流动非流动负债组成分析:")
    print('a.'+string + "流动负债占比：", f.percentageOccupied(d.current_liability, d.total_liability))
    print('b.'+string + "非流动负债占比：", f.percentageOccupied(d.non_current_liability, d.total_liability))
    print('c.'+string + "流动负债主要组成分析(前三项):")
    current_liability_composition = f.component_analysis(d.cl_no+1, d.current_liability_no)
    for i in range(len(d.years)):
        print(str(d.years[i]), current_liability_composition[i])
    print('d.'+string + "非流动负债主要组成分析(前三项):")
    non_current_liability_composition = f.component_analysis(d.ncl_no+1, d.non_current_liability_no)
    for i in range(len(d.years)):
        print(str(d.years[i]), non_current_liability_composition[i])


def profit_analysis():
    gross_profit = [r-o for r, o in zip(d.revenue, d.operating_expense)]
    period_expense = []
    for i in range(len(d.selling_expense)):
        period_expense.append(
            sum([d.selling_expense[i], d.management_expense[i], d.financing_expense[i]]))
    print("二、利润表分析:")
    print("1.基本信息:")
    print(string + '营业收入:', [round(i, 2) for i in d.revenue])
    print(string + '营业成本:', [round(i, 2) for i in d.operating_expense])
    print(string + '营业成本增长率', f.percentageChange(d.operating_expense))
    print(string + '营业利润', [round(no, 2) for no in d.operating_profit])
    print(string + '营业利润变化', f.percentageChange(d.operating_profit))
    print(string + '净利润', [round(no, 2) for no in d.net_profit])
    print(string + '净利润变化', f.percentageChange(d.net_profit))
    print(string + '销售费用', [round(no, 2) for no in d.selling_expense])
    print(string + '管理费用', [round(no, 2) for no in d.management_expense])
    print(string + '财务费用', [round(no, 2) for no in d.financing_expense])
    print(string + '期间费用', [round(no, 2) for no in period_expense])
    print(string + '期间费用变化', f.percentageChange(period_expense))
    print(string + '三费占比', f.percentageOccupied(period_expense, d.revenue))
    print("2. 利润结构分析数据:")
    print(string + '营业利润占比利润总额', f.percentageOccupied(d.operating_profit, d.overall_profit))
    print(string + '毛利', gross_profit)
    print(string + '毛利率', f.ratio(gross_profit, d.revenue))
    print(string + '毛利率变化', f.percentageChange(f.ratio(gross_profit, d.revenue)))


def cashflow_analysis():
    print("三、现金流量表分析:")
    print("1. 基本信息:")
    print(string + '经营活动产生的现金流入小计', [round(i, 2) for i in d.operation_ttinflow])
    print(string + '经营活动产生的现金流出小计', [round(i, 2) for i in d.operation_ttoutflow])
    print(string + '经营活动产生的现金流量', [round(i, 2) for i in d.operation_cashflow])
    print(string + '经营现金净流量增长率', f.percentageChange(d.operation_cashflow))

    print(string + '投资活动产生的现金流入小计', [round(i, 2) for i in d.investment_ttinflow])
    print(string + '投资活动产生的现金流出小计', [round(i, 2) for i in d.investment_ttoutflow])
    print(string + '投资活动产生的现金流量', [round(i, 2) for i in d.investment_cashflow])
    print(string + '投资活动产生的现金流量变化', f.percentageChange(d.investment_cashflow))

    print(string + '筹资活动产生的现金流入小计', [round(i, 2) for i in d.financing_ttinflow])
    print(string + '筹资活动产生的现金流出小计', [round(i, 2) for i in d.financing_ttoutflow])
    print(string + '筹资活动产生的现金流量', [round(i, 2) for i in d.financing_cashflow])
    print(string + '筹资活动产生的现金流量变化', f.percentageChange(d.financing_cashflow))

    print("2. 企业销售利润、销售回款和创现能力（公司销售商品提供劳务收到的现金与购进劳务付出的现金比）:",
          f.ratio(d.operation_inflow, d.operation_outflow))
    print("3. 企业的主营业务与营销状况（销售商品提供劳务产生的现金流入于流入现金总额占比）:",
          f.percentageOccupied(d.operation_inflow, d.operation_ttinflow))
    print("4. 现金流入组成：", f.percentage_compostion([d.operation_ttinflow, d.investment_ttinflow,
                                                 d.financing_ttinflow]))
    print("5. 现金流出组成：")
    print("6. 净现金流量总量分析：")
    print(string + "净现金流量总量 ", [round(i, 2) for i in d.total_cashflow])
    print(string + "净现金流量总量变化率 ", f.percentageChange(d.total_cashflow))
    print(string + "经营现金流量占比 ", f.percentageOccupied(d.operation_cashflow, d.total_cashflow))
    print(string + "投资现金流量占比 ", f.percentageOccupied(d.investment_cashflow, d.total_cashflow))
    print(string + "筹资先金流量占比 ", f.percentageOccupied(d.financing_cashflow, d.total_cashflow))


def ratio_analysis():
    print("1. 短期偿债能力:")
    print(string + '流动比率', f.ratio(d.current_asset, d.current_liability))
    print(string + '速动比率', f.ratio(d.quick_asset, d.current_liability))
    print("2. 长期负债能力:")
    print(string + '资产负债率', f.percentageOccupied(d.total_liability, d.total_asset))
    print(string + '股东权益比率', f.percentageOccupied(d.owner_equity, d.total_asset))
    print(string + '权益乘数', f.percentageOccupied(d.total_asset, d.owner_equity))
    print(string + '产权比率', f.percentageOccupied(d.total_liability, d.owner_equity))
    print("3.发展能力:")
    print(string + '净资产增长率', f.percentageChange(d.owner_equity))
    print(string + '销售增长率', f.percentageChange(d.revenue))
    print(string + '总资产增长率', f.percentageChange(d.total_asset))
    print("4. 盈利能力分析数据:")
    print(string + '销售净利率', f.percentageOccupied(d.net_profit, d.revenue))
    print(string + '总资产收益率', f.percentageOccupied(d.net_profit, d.total_asset))
    print(string + '净资产收益率', f.percentageOccupied(d.net_profit, d.owner_equity))


# def plot_analysis():
#     title1 = string + ' Asset Situation'
#     title2 = string + ' Liability Situation'
#     title3 = string + ' Current Asset Composition(Top Three)'
#     title4 = string + ' Non-current Asset Composition(Top Three)'
#     title5 = string + '  Current Liability Composition(Top Three)'
#     title6 = string + '  Non-current liability Composition(Top Three)'
#     title7 = string + ' cash inflow compostion'
#     title8 = string + ' cash outflow composition'
#     print("1.资产组成(如图):")
#     percentagePlot([current_asset, non_current_asset], [
#         "current asset", "non current asset"], title1)
#     print("2.负债组成(如图):")
#     percentagePlot([current_liability, non_current_liability], [
#         "current liability", "non current liability"], title2)
#     print("3.流动资产主要组成分析(前三项)(如图):")
#     componentPlot(ca_no+1, current_asset_no, title3)
#     print("4.非流动资产主要组成分析(前三项)(如图):")
#     componentPlot(nca_no+1, non_current_asset_no, title4)
#     print("5.流动负债主要组成分析(前三项)(如图):")
#     componentPlot(cl_no+1, current_liability_no, title5)
#     print("6.非流动负债主要组成分析(前三项)(如图):")
#     componentPlot(ncl_no+1, non_current_liability_no, title6)
#     print("7.现金流入组成：")
#     percentagePlot([operation_ttinflow, investment_ttinflow,
#                     financing_ttinflow], ['o', 'i', 'f'], title7)
#     print("8.现金流出组成：")
#     percentagePlot([operation_ttoutflow, investment_ttoutflow,
#                     financing_ttoutflow], ['o', 'i', 'f'], title8)


# def componentPlot(start, end, title):
#     component = []
#     legend = sheet.col_values(0, start_rowx=start, end_rowx=end)
#     for i in range(1, len(years)+1):
#         component.append(sheet.col_values(i, start_rowx=start, end_rowx=end))
#     tobeplot = []
#     new_legend = []
#     for i in range(len(component)):
#         dictionary = dict(zip(legend, component[i]))
#         dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
#         label = [x[0] for x in dictionary][:3]
#         label.append('others')
#         new_component = [x[1] for x in dictionary][:3]
#         other_component = sum([x[1]for x in dictionary])-sum(new_component)
#         new_component.append(other_component)
#         tobeplot.append(new_component)
#         new_legend.append(label)
#     for i in range(len(tobeplot)):
#         print(dict(zip(new_legend[i], [round(a, 2) for a in tobeplot[i]])))
#     fig, ax = plt.subplots(1, len(years))
#     for i in range(len(years)):
#         wedges, texts, autotexts = ax[i].pie(
#             tobeplot[i], autopct='%1.1f%%', textprops=dict(color="black"))
#         ax[i].set_title(str(years[i]), loc='center')
#         ax[i].legend(wedges, new_legend[i], loc=8, bbox_to_anchor=(
#             0.5, -0.5), fancybox=True, shadow=True)
#         plt.setp(autotexts, size=6, weight="bold")
#     fig.suptitle(title)
#     fig.tight_layout()
#     plt.show()
