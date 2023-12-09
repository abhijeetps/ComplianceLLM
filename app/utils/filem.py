import os
from app.consts import RESULTS_DIR


def init(cwd):
    if not os.path.exists(RESULTS_DIR):
        print(f"Creating directory #{RESULTS_DIR}")
        os.makedirs(cwd + '/' + RESULTS_DIR)
    else:
        print("Directory already exists. Skipping directory creation.")

def write_to_file(cwd, data, type="compliance_report"):
    if type == 'compliance_policy':
        try:
            file = open(cwd + '/' + RESULTS_DIR + '/' + 'compliance_policy.txt', 'w')
            file.writelines(data)
            file.close()
        except Exception as e:
            print(f"Error occured while trying to write compliance policy: #{e}" )

    elif type == "compliance_report":
        try:
            file = open(cwd + '/' + RESULTS_DIR + '/' + 'compliance_report.txt', 'w')
            file.writelines(data)
            file.close()
        except Exception as e:
            print(f"Error occured while trying to write compliance report: #{e}" )

def read_compliance_policy(cwd):
    try:
        file = open(cwd + '/' + RESULTS_DIR + '/' + 'compliance_policy.txt', 'r')
        content = file.readlines()
        file.close()
        return content
    except Exception as e:
        print(f"Error reading compliance policy. #{e}")
