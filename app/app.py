from app.utils.scrap import scrap
from app.utils.filem import write_to_file, read_compliance_policy
from app.apis.llm import use_llm

def do_compliance_website(cwd, compliance_website_url):
    print("Scrapping compliance website.")
    compliance_policy = scrap(compliance_website_url, type="compliance_website")
    print("Finished scrapping compliance website.")

    print("Writing compliance policy.")
    write_to_file(cwd, compliance_policy, type="compliance_policy")
    print("Finished writing compliance policy.")

def do_test_content(cwd, to_test_website):
    print("Scrapping to test website.")
    to_test_content = scrap(to_test_website)
    print("Finished scrapping to test website.")
    compliance_policy = read_compliance_policy(cwd)

    print("Testing website against compliance policy.")
    report = use_llm(compliance_policy, to_test_content)
    print("Finished testing website against compliance policy.")

    print("Generating Report")
    write_to_file(cwd, report)
    print("Finished generating report")

    return report
