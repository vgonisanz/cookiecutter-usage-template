import sys

from cookiecutter.main import cookiecutter

def clone_helloworld(url, path, name):
    print("Cloning %s at path %s from %s" % (name, path, url))
    cookiecutter(url, no_input=True, output_dir=path)
    return

if __name__ == "__main__":
    print("Posthook for {{ cookiecutter.project_name}}")

    # jinja syntax
    {% if cookiecutter.add_hello_world == "yes" %}
    clone_helloworld("https://github.com/vgonisanz/cookiecutter-helloworld.git", "greeting", "hi")
    {% endif %}

    {% for module in cookiecutter.modules.names %}
    print("Creating module: {{module}}")
    {% endfor %}

    {% for sample in cookiecutter.samples.names %}
    print("Creating sample: {{sample}}")
    {% endfor %}

    exit(0)
