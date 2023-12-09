import os
from flask import Flask, request
from app.app import do_compliance_website, do_test_content
from app.utils.filem import init
app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_request_compliance_website():
    cwd = os.getcwd()
    init(cwd)
    print("Received POST request on path '/' with data: %s" % (request.form))

    compliance_website_url = request.form["compliance_website"]
    do_compliance_website(cwd, compliance_website_url)

    to_test_website = request.form["to_test_website"]
    report = do_test_content(cwd, to_test_website)

    return report

if __name__ == "__main__":
    app.run()
