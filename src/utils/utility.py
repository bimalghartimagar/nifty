""" Utility module with helper functions """


def clean_escaped_strings(dirty):
    return dirty.replace('\n', '').replace('\t', '')


def rate_sort(rate_dict):
    return float(rate_dict['rate'])


def calc_diff(rates):

    for i in range(len(rates)):
        if i == 0:
            rates[i]['diff'] = '-'
        else:
            rates[i]['diff'] = round(((rates[i].get('rate') - rates[0].get('rate'))/rates[0].get('rate'))*100, 2)
    return rates
