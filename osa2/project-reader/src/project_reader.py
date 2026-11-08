from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        config = tomli.loads(content)
        #print(config)
        return Project(config["project"]["name"],
                       config["project"]["description"],
                       config["project"]["license"],
                       config["project"]["authors"],
                       config["project"]["dependencies"],
                       config["dependency-groups"]["dev"])
