# Docker LPT

Image for writing documents, generating plots and data manipulation [@LPT](https://www.unibw.de/plasmatechnik). Requires [docker](https://docs.docker.com/get-docker/) for building.

## Build

Inside a terminal in this folder, run (recommended):

```sh
docker build -t pandoc-lpt .
```

or pull directly from the Hub

```sh
docker pull mmaigler/docker-lpt
```

## Examples

* [Letter](https://gitlab.com/mb-42/infrastructure/templates/administration/letter)
* [Bachelor- / Master- / Studentenarbeit](https://gitlab.com/mb-42/infrastructure/templates/studenten/bms)
* [Technical report](https://gitlab.com/mb-42/infrastructure/templates/reports/technical-report)
* Articles
  - AIAA
  - STAB