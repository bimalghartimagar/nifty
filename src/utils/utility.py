def clean_escaped_strings(dirty):
    return dirty.replace('\n','').replace('\t','')

def rate_sort(rate_dict):
    return float(rate_dict['rate'])