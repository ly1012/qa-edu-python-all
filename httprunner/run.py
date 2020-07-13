from httprunner.api import HttpRunner

runner = HttpRunner(log_level="INFO")
runner.run(r'testcases/login_testcase.yml')