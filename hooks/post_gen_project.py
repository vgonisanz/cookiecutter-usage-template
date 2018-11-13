import sys

from cookiecutter.main import cookiecutter

def clone_another():
    print("Cloning another cookiecutter project")
    cookiecutter('https://github.com/Catacrockers/cookiecutter-helloworld.git',
                    no_input=True)
    return

if __name__ == "__main__":
    print("Posthook for {{ cookiecutter.project_name}}")

    # jinja syntax
    {%- if cookiecutter.add_hello_world == "yes" -%}
    clone_another()
    {% endif %}

    {% for module in cookiecutter.modules.names %}
    print("Creating module: {{module}}")
    {% endfor %}

    {% for sample in cookiecutter.samples.names %}
    print("Creating sample: {{sample}}")
    {% endfor %}

    exit(0)
