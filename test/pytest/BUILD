package(
    python = {
        "TEST_RUNNER": "pytest",
        "TESTRUNNER_DEPS": "///python_rules//third_party/python:pytest_bootstrap",
    },
)

python_test(
    name = "foo",
    srcs = ["test.py"],
    deps = ["//src:add"],
)
