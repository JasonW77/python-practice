def load_template(filename):
    with open(filename, 'r') as file:
        return file.read()

def get_placeholders(template):
    import re
    return re.findall(r'{(.*?)}', template)

def get_user_inputs(placeholders):
    inputs = {}
    for ph in placeholders:
        user_input = input(f"Enter a {ph.replace('_', ' ')}: ")
        inputs[ph] = user_input
    return inputs

def fill_template(template, inputs):
    return template.format(**inputs)

def main():
    template = load_template('mad_libs_template.txt')
    placeholders = get_placeholders(template)
    user_inputs = get_user_inputs(placeholders)
    final_story = fill_template(template, user_inputs)

    print("\n🎉 Your Mad Libs Story:")
    print("-" * 40)
    print(final_story)

if __name__ == "__main__":
    main()
