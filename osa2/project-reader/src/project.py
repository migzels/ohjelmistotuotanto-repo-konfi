import re

class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        new_deps = "".join(f"\n- {re.split(r'[>=<]',dep,)[0]}" for dep in dependencies)
        return new_deps if len(new_deps) > 0 else "-"

    def __str__(self):

        authors_str = "".join(f"\n- {author['name']}" for author in self.authors)
        new_deps = "".join(f"\n- {re.split(r'[>=<]',dep,)[0]}" for dep in self.dependencies)

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:"
            f"{authors_str}"
            f"\n\nDependencies:"
            f"\n- python"
            f"{self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies:"
            f"{self._stringify_dependencies(self.dev_dependencies)}"
        )
