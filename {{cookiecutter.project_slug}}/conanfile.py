from conans import (
    ConanFile,
    python_requires,
    tools,
)


b2 = python_requires("b2-helper/[>=0.7.1]@grisumbras/stable")

@b2.build_with_b2
class {{cookiecutter.project_name.title().replace("-", "").replace(" ", "")}}Conan(ConanFile):
    name = "{{cookiecutter.project_slug}}"
    license = "BSL-1.0"
    description = "{{cookiecutter.project_description}}"
    homepage = "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}"
    url = homepage

    author = "{{cookiecutter.full_name}} <{{cookiecutter.email}}>"
    default_user = "{{cookiecutter.conan_username}}"
    default_channel = "testing"

    exports_sources = "build.jam", "LICENSE"
    no_copy_source = True

    def set_version(self):
        import re

        content = tools.load("build.jam")
        match = re.search(r"constant\s*VERSION\s*:\s*(\S+)\s*;", content)
        self.version = match.group(1)

    def package_id(self):
        self.info.header_only()
