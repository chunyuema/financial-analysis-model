from matplotlib import pyplot as plt
import data as d


def percentageChange(list):
    pc_change = ['--']
    for i in range(len(list)-1):
        previous = list[i]
        current = list[i+1]
        if previous == 0 or previous == '--' or current == '--':
            pc_change.append('--')
        else:
            change = round(((current-previous)/abs(previous))*100, 2)
            pc_change.append(str(change)+'%')
    return pc_change


def percentageOccupied(l1, l2):
    # return a list of strings
    pc_occupied = []
    for i in range(len(l1)):
        if l2[i] == 0 or l2[i] == '--' or l1[i] == '--':
            pc_occupied.append('--')
        else:
            p = str(round(l1[i]/l2[i]*100, 2))
            pc_occupied.append(p + '%')
    return pc_occupied


def ratio(l1, l2):
    # return a list of numbers
    ratio = []
    for i in range(len(l1)):
        if l2[i] == 0 or l2[i] == '--' or l1[i] == '--':
            ratio.append('--')
        else:
            r = round(l1[i]/l2[i], 2)
            ratio.append(r)
    return ratio


def percentage_compostion(list):
    total = []
    for i in range(len(d.years)):
        sum = 0
        for item in list:
            sum += item[i]
        total.append(sum)
    return total


def percentagePlot(tobeplot, legend, title):
    # tobeplot: a list containing lists to be ploted
    # legend: a list of strings specifying legend to be put on the graph
    # title: a string specifying the title of the graph
    fig, ax = plt.subplots(1, len(d.years))
    for i in range(len(d.years)):
        plot = [list[i] for list in tobeplot]
        print(plot)
        wedges, texts, autotexts = ax[i].pie(
            plot, autopct='%1.1f%%', textprops=dict(color="black"))
        ax[i].set_title(str(d.years[i]), loc='center')
        plt.setp(autotexts, weight="bold")
    fig.suptitle(title)
    fig.legend(legend, loc=0)
    fig.tight_layout()
    plt.show()


def component_analysis(start, end):
    component = []
    total = []
    legend = d.sheet.col_values(0, start_rowx=start, end_rowx=end)
    for i in range(1, len(d.years)+1):
        values = d.sheet.col_values(i, start_rowx=start, end_rowx=end)
        component.append(values)
        total.append(sum(d.sheet.col_values(i, start_rowx=start, end_rowx=end)))
    component_percentage = []
    result = []
    for i in range(len(component)):
        component_percentage = percentageOccupied(component[i], [total[i]]*len(component[i]))
        component_percentage2 = percentageOccupied(
            component[i], [d.total_asset[i]]*len(component[i]))
        a = list(zip(legend, [round(j, 2) for j in component[i]], component_percentage))
        # b = list(zip(legend, [round(j, 2) for j in component[i]], component_percentage2))
        asort = sorted(a, key=lambda tup: tup[1], reverse=True)
        # bsort = sorted(b, key=lambda tup: tup[1], reverse=True)
        result.append(asort[:3])
    # print(str(d.years[i])+'总占比', bsort[:3])
    return result


current_asset_component = component_analysis(d.ca_no+1, d.current_asset_no)
revenue_change = percentageChange(d.revenue)
total_asset_change = percentageChange(d.total_asset)
total_liability_change = percentageChange(d.total_liability)
liability_asset_ratio = ratio(d.total_liability, d.total_asset)
liability_asset_ratio_change = percentageChange(liability_asset_ratio)
operating_expense_change = percentageChange(d.operating_expense)
selling_expense_change = percentageChange(d.selling_expense)
management_expense_change = percentageChange(d.management_expense)
financing_expense_change = percentageChange(d.financing_expense)
net_profit_change = percentageChange(d.net_profit)
operation_cashflow_change = percentageChange(d.operation_cashflow)
investment_cashflow_change = percentageChange(d.investment_cashflow)
financing_cashflow_change = percentageChange(d.financing_cashflow)
