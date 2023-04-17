#!/usr/bin/python3
"""\
This script contains helper functions for
pandoc pre-processing
"""

# 3rd party packages
import yaml
import os
import sys
import string

class Pandoc:

    def __init__(self, meta_data, journal):
        self.meta = self.readMeta(meta_data)

    def readMeta(self, meta_data):
        with open(meta_data, "r") as f:
            return yaml.safe_load(f)

    def MDPI(self):
        alphabet = list(string.ascii_uppercase)
        
        author_str = ""

        a = 0
        # First find orcid
        for authors in self.meta["authors"]:
            if "orcid" in authors:
                author_str += "\n" + r"""\newcommand{\orcidauthor%s}{%s}""" % (alphabet[a], authors["orcid"])
                a += 1

        a = 0
        # Next find authors
        author_str += "\n\n" + r"""\Author{""" + "\n"
        for authors in self.meta["authors"]:
            author_str += r"""  %s %s $$^{%s,\dagger,\ddagger}$$""" % (
                authors["name"]["given"],
                authors["name"]["surname"],
                authors["affiliation"]
            )
            if "orcid" in authors:
                author_str += "\n" + r"""  \orcid%s{},""" % alphabet[a] + "\n"
                a += 1
            author_str += "\n"
            
        # Add 'MDPI internal command: Authors, for metadata in PDF
        author_str += "}\n\n" + r"""\AuthorNames{"""
        i = 0
        num_authors = len(self.meta["authors"])
        for authors in self.meta["authors"]:
            if i + 1 == num_authors:
                author_str += authors["name"]["given"] + " " + authors["name"]["surname"] + "}"
            elif i + 2 == num_authors:
                author_str += authors["name"]["given"] + " " + authors["name"]["surname"] + " and "
            else:
                author_str += authors["name"]["given"] + " " + authors["name"]["surname"] + ", "
            i += 1

        # MDPI internal command: Authors, for citation in the left column
        i = 0
        author_str += "\n\n" + r"""\AuthorCitation{"""
        for authors in self.meta["authors"]:
            if i + 1 == num_authors:
                author_str += authors["name"]["surname"] + ", " + authors["name"]["given"][0] + ".}"
            else:
                author_str += authors["name"]["surname"] + ", " + authors["name"]["given"][0] + ".; "
            i += 1
        
        # Affiliations
        iAffil = 1
        num_affils = len(self.meta["affiliations"])
        author_str += "\n\n" + r"""\address{""" + "\n"
        for affils in self.meta["affiliations"]:
            if num_affils == 1:
                author_str += r"""$$^{%s}$$""" % iAffil + r" \quad %s, %s, %s, %s, %s; %s" % (
                    affils["name"],
                    affils["address"]["street"],
                    affils["address"]["postcode"],
                    affils["address"]["city"],
                    affils["address"]["country"],
                    affils["email"],
                    ) + "\n}"
            else:
                if iAffil == num_affils:
                    author_str += r"""$$^{%s}$$""" % iAffil + r" \quad %s, %s, %s, %s, %s; %s" % (
                        affils["name"],
                        affils["address"]["street"],
                        affils["address"]["postcode"],
                        affils["address"]["city"],
                        affils["address"]["country"],
                        affils["email"],
                        ) + "\n}"
                else:
                    author_str += r"""$$^{%s}$$""" % iAffil + r" \quad %s, %s, %s, %s, %s; %s\\" % (
                        affils["name"],
                        affils["address"]["street"],
                        affils["address"]["postcode"],
                        affils["address"]["city"],
                        affils["address"]["country"],
                        affils["email"],
                        ) + "\n"
                iAffil += 1

        # Correspondence
        for authors in self.meta["authors"]:
            if "correspondence" in authors:
                author_str += "\n\n" + r"""\corres{Correspondece: """ + authors["correspondence"]["email"] + "; Tel.: " + authors["correspondence"]["tel"] + "}\n"
                break

        # with open("/root/.local/share/pandoc/templates/mdpi.latex", "r") as f:
        with open("mdpi.latex", "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line[:-1] == r"% Authors":
                lines[i] += author_str[1:]

        with open("mdpi2.latex", "w") as f:
            f.writelines(lines)

            


if __name__ == "__main__":

    args = list(sys.argv)
    journal = args[1]
    pandoc_object = Pandoc("meta.yaml", journal)
    eval(f"pandoc_object.{journal}()")
    # pandoc_object.export()