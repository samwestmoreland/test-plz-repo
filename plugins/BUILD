# subinclude("@python_rules//build_defs:python")

github_repo(
    name = "python_rules",
    repo = "samwestmoreland/python-rules",
    revision = "b3a8e21c0fd5ce629e54bbe96ee75d11e4af1634",
)

# github_repo(
#     name = "cc_rules",
#     repo = "please-build/cc-rules",
#     revision = "1dddaf2c17f8d3c5d9f330541280d7f6e018097d",
# )

subrepo(
    name = "cc_rules",
    dep = build_rule(
            name = "cc_rules",
            system_srcs = ["/home/swestmoreland/cc-rules"],
            cmd = "cp -r /home/swestmoreland/cc-rules $OUT",
            outs = ["cc_rules"],
            _subrepo = True,
        ),
) 

# plugin_repo(
#     name = "cc_rules",
#     revision = "",
#     owner = "samwestmoreland",
# )
