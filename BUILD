# subinclude("@python_rules//build_defs:python")

github_repo(
    name = "python_rules",
    repo = "samwestmoreland/python-rules",
    revision = "e1edbf61d427a5867fcb371fd82e14187176e44d",
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
            system_srcs = ["/Users/swestmoreland/git_repos/cc-rules"],
            cmd = "cp -r /Users/swestmoreland/git_repos/cc-rules/ $OUT",
            outs = ["cc_rules"],
            _subrepo = True,
        ),
) 
