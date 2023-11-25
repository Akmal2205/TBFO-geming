import re

def attribute_generalizer(string):
    pattern_src = re.compile(r'src="[^"]+"')
    pattern_alt = re.compile(r'alt="[^"]+"')
    pattern_href = re.compile(r'href="[^"]+"')
    pattern_id = re.compile(r'id="[^"]+"')
    pattern_class = re.compile(r'class="[^"]+"')
    pattern_style = re.compile(r'style="[^"]+"')
    result_string = pattern_src.sub('src="*"', string)
    result_string = pattern_alt.sub('alt="*"', result_string)
    result_string = pattern_href.sub('href="*"', result_string)
    result_string = pattern_id.sub('id="*"', result_string)
    result_string = pattern_class.sub('class="*"', result_string)
    result_string = pattern_style.sub('style="*"', result_string)
    return result_string

print(attribute_generalizer('    <div id="footer" class="footer"> This is the end of the page </div>'))