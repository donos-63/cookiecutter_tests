import os
import sys
import subprocess


# we don't use celery. keep as an example
print(">>>>>>  post installation processing  <<<<<<")
local_path = os.getcwd()
print(local_path)

print(">>>>>>  install requirements")
subprocess.run(
    [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        os.path.join(local_path, "requirements.txt"),
    ]
)
subprocess.run(
    [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
    cwd=os.path.join(local_path, "src", "application"),
)

print(">>>  Setup db")
subprocess.run(
    [sys.executable, "-m", "flask", "db", "upgrade"],
    cwd=os.path.join(local_path, "src", "application"),
)

print(">>>  setup application")
subprocess.run(
    [sys.executable, "-m", "flask", "{{cookiecutter.app_name}}", "init"],
    cwd=os.path.join(local_path, "src", "application"),
)

print(">>>  test installation")
subprocess.run(
    [sys.executable, "-m", "tox", "-e", "test"],
    cwd=os.path.join(local_path, "src", "application"),
)


print(">>>>>>  post installation end  <<<<<<")
