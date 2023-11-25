import re

def format_src_attribute(text):
    # Define the regex pattern to match 'src = "any string"' or 'src="any string"'
    pattern = re.compile(r'src\s*=\s*("[^"]*")')

    # Replace the pattern with 'src="any string"'
    formatted_text = pattern.sub(r'src=\1', text)
    return formatted_text

# Example usage:
input_text = 'src = "Hello World"'
formatted_output = format_src_attribute(input_text)
print(formatted_output)