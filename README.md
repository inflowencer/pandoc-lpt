# pandoc-lpt

Pandoc image for documents written in Markdown and YAML into LaTeX and Word. Requires [docker](https://docs.docker.com/get-docker/) for building.

## Build

Inside a terminal, run:

```sh
docker pull mmaigler/pandoc-lpt
```

or search (`CTRL+k`) in the GUI: `pandoc-lpt`. Alternatively, you can build the image by yourself by running

```sh
docker build -t pandoc-lpt .
```

inside this directory.

## Examples

* [Letter](https://gitlab.com/mb-42/infrastructure/templates/administration/letter)
* [Bachelor- / Master- / Studentenarbeit](https://gitlab.com/mb-42/infrastructure/templates/studenten/bms)
* [Technical report](https://gitlab.com/mb-42/infrastructure/templates/reports/technical-report)
* Articles
  - AIAA
  - STAB