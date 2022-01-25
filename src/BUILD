# subinclude("@python_rules//build_defs:python")
# 
python_library(
        name = "add",
        srcs = ["foo.py"],
        visibility = ["PUBLIC"],
)

genrule(
    name = "foo",
    cmd = ["echo 'Blah'"],
)
