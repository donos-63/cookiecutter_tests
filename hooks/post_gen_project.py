import os
import sys
import shutil
import subprocess


#we don't use celery. keep as an example
print("post installation processing")
local_path = os.getcwd()
print(local_path)

print("install requirements")
subprocess.check_call([sys.executable, "-m", "pip", "install", os.path.join(local_path, "{{ cookiecutter.project_name }}", 'requirements.txt')])
subprocess.check_call([sys.executable, "-m", "pip", "install", os.path.join(local_path, "{{ cookiecutter.project_name }}", 'src', 'application', 'requirements.txt')])
""" 
print("initialize db")
subprocess.check_call([sys.executable, "-m", "flask", "db upgrade", cwd=os.path.join(local_path, {{ cookiecutter.project_name }}, 'src', 'application', 'requirements.txt')])

print("initialize application")
subprocess.check_call([sys.executable, "-m", "flask", "init {{cookiecutter.app_name}}", os.path.join(local_path, {{ cookiecutter.project_name }}, 'src', 'application', 'requirements.txt')])
 """


print("post installation end")

""" 
use_celery = '--cookiecutter.use_celery--'


if use_celery == "no":
    base_path = os.getcwd()
    app_path = os.path.join(
        base_path,
        '{{cookiecutter.app_name}}',
    )
    tasks_path = os.path.join(app_path, 'tasks')
    celery_app_path = os.path.join(app_path, 'celery_app.py')

    try:
        shutil.rmtree(tasks_path)
    except Exception:
        print("ERROR: cannot delete celery tasks path %s" % tasks_path)
        sys.exit(1)

    try:
        os.remove(celery_app_path)
    except Exception:
        print("ERROR: cannot delete celery application file")
        sys.exit(1)

    try:
        os.remove(os.path.join(base_path, "tests", "test_celery.py"))
    except Exception:
        print("ERROR: cannot delete celery tests files")
        sys.exit(1)
 """