import sys

from cookiecutter.main import cookiecutter

def clone_another():
    print("Cloning another cookiecutter project")
    cookiecutter('https://github.com/Catacrockers/cookiecutter-helloworld.git',
                    no_input=True)
    return

if __name__ == "__main__":
    print("Posthook for {{ cookiecutter.project_name}}")
    clone_another()
    exit(0)
