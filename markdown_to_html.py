import re

def markdown_to_html(markdown_text):
        # Convert headers
    markdown_text = re.sub(r'###### (.*)', r'<h6>\1</h6>', markdown_text)
    markdown_text = re.sub(r'##### (.*)', r'<h5>\1</h5>', markdown_text)
    markdown_text = re.sub(r'#### (.*)', r'<h4>\1</h4>', markdown_text)
    markdown_text = re.sub(r'### (.*)', r'<h3>\1</h3>', markdown_text)
    markdown_text = re.sub(r'## (.*)', r'<h2>\1</h2>', markdown_text)
    markdown_text = re.sub(r'# (.*)', r'<h1>\1</h1>', markdown_text)

    # Bold and Italics
    markdown_text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', markdown_text)
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_text)
    markdown_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown_text)

    # Links
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown_text)

    # Unordered list items
    markdown_text = re.sub(r'^\* (.*)', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)

    return markdown_text

def convert_file(input_path, output_path):
    with open(input_path, 'r') as f:
        md_text = f.read()
        html = markdown_to_html(md_text)
        with open(output_path, 'w') as f:
            f.write(html)
        print(f"✅ Converted '{input_path}' to '{output_path}'.")

if __name__ == "__main__":
    input_md = "sample.md"
    output_html = "output.html"
    convert_file(input_md, output_html)