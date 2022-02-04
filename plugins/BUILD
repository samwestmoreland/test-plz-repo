# subinclude("@python_rules//build_defs:python")

# plugin_repo(
#     name = "python_rules",
#     plugin = "python-rules",
#     revision = "1085dbffab7f9d8f2ebddd5d7555b074c907d3a3",
#     owner = "please-build",
# )

subrepo(
    name = "python_rules",
    dep = build_rule(
            name = "python_rules",
            system_srcs = ["/home/swestmoreland/python-rules"],
            cmd = "cp -r /home/swestmoreland/python-rules $OUT",
            outs = ["python_rules"],
            _subrepo = True,
        ),
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

plugin_repo(
  name = "python",
  revision = "v0.2.0",
  plugin = "python-rules",
  owner = "please-build",
)
