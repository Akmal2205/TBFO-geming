import re

def attribute_generalizer(string):
    pattern_src = re.compile(r'src\s*=\s*["\'][^"\']*["\']')  # Updated pattern for src attribute
    pattern_alt = re.compile(r'alt\s*=\s*["\'][^"\']*["\']')
    pattern_href = re.compile(r'href\s*=\s*["\'][^"\']*["\']')
    pattern_id = re.compile(r'id\s*=\s*["\'][^"\']*["\']')
    pattern_class = re.compile(r'class\s*=\s*["\'][^"\']*["\']')
    pattern_style = re.compile(r'style\s*=\s*["\'][^"\']*["\']')
    pattern_action = re.compile(r'action\s*=\s*["\'][^"\']*["\']')
    pattern_type = re.compile(r'type\s*=\s*("[^"]*")')
    pattern_method = re.compile(r'method\s*=\s*("[^"]*")')
    pattern_rel = re.compile(r'rel\s*=\s*("[^"]*")')
    pattern_comment = re.compile(r'<!--.*?-->')

    result_string = pattern_src.sub('src=*', string)
    result_string = pattern_rel.sub('rel=*', result_string)
    result_string = pattern_comment.sub('cmd', result_string)
    result_string = pattern_alt.sub('alt=*', result_string)
    result_string = pattern_href.sub('href=*', result_string)
    result_string = pattern_id.sub('id=*', result_string)
    result_string = pattern_class.sub('class=*', result_string)
    result_string = pattern_style.sub('style=*', result_string)
    result_string = pattern_action.sub('action=*', result_string)
    result_string = pattern_method.sub(r'method=\1', result_string)
    result_string = pattern_type.sub(r'type=\1', result_string)

    return result_string

print(attribute_generalizer('src=""'))