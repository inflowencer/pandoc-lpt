FROM dalibo/pandocker:latest

LABEL version="0.1"
LABEL description="Pandoc image for documents of MB42"

# Build arguments
ARG TEXMFHOME=/root/texmf
ARG PANDOC_TEX_RES=${TEXMFHOME}/tex/latex/pandoc/
ARG PANDOC_TEMPLATES=/root/.local/share/pandoc/templates
ARG PANDOC_RESOURCES=/root/resources

RUN sed -i 's/htt[p|ps]:\/\/archive.ubuntu.com\/ubuntu\//mirror:\/\/mirrors.ubuntu.com\/mirrors.txt/g' /etc/apt/sources.list
RUN apt-get update && apt-get install lua5.4 fonts-firacode
# Install custom packages, update accordingly
RUN	tlmgr install latexmk translations siunitx caption float subfig amsmath graphics acro multirow \
  tools lipsum setspace fancyhdr lastpage bookmark vhistory ragged2e titlesec fontspec lstfiracode \
  mhchem advdate acronym bigfoot xstring
RUN	tlmgr update --all

# pandoc and LaTeX folders
RUN  mkdir -p ${PANDOC_TEMPLATES} ${PANDOC_TEX_RES} ${PANDOC_RESOURCES}/logo ${PANDOC_RESOURCES}/csl
COPY templates/classes/* ${PANDOC_TEX_RES}/.
COPY templates/pandoc/* ${PANDOC_TEMPLATES}/.
COPY templates/csl/*  ${PANDOC_RESOURCES}/csl/.
COPY templates/logo/* ${PANDOC_RESOURCES}/logo/.


ENTRYPOINT [ "/bin/bash", "-l", "-c" ]


# SCRATCH:
# ARG PANDOC_FILTERS=/root/.local/share/pandoc/filters
# COPY templates/filters/* ${PANDOC_FILTERS}/.