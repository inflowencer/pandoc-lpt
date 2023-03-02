FROM dalibo/pandocker:latest

LABEL version="0.2"
LABEL description="Document geration, plotting and data manipulation of LPT"

RUN mkdir -p /root/.fonts
COPY src/fonts/Avenir.ttf /root/.fonts/.

# Build arguments
ARG TEXMFHOME=/root/texmf
ARG PANDOC_TEX_RES=${TEXMFHOME}/tex/latex/pandoc/
ARG PANDOC_TEMPLATES=/root/.local/share/pandoc/templates
ARG PANDOC_RESOURCES=/root/resources

RUN sed -i 's/htt[p|ps]:\/\/archive.ubuntu.com\/ubuntu\//mirror:\/\/mirrors.ubuntu.com\/mirrors.txt/g' /etc/apt/sources.list
RUN apt-get update && apt-get install lua5.4 fonts-firacode python3-pip
# Install custom packages, update accordingly
RUN	tlmgr install latexmk translations siunitx caption float subfig amsmath graphics acro multirow \
  tools lipsum setspace fancyhdr lastpage bookmark vhistory ragged2e titlesec fontspec lstfiracode \
  mhchem advdate acronym bigfoot xstring newtx fontaxes preprint lettrine minifp quoting tex-gyre \
  txfonts
RUN	tlmgr update --all
RUN pip3 install matplotlib pandas numpy scipy h5py pyyaml

# pandoc and LaTeX folders
RUN  mkdir -p ${PANDOC_TEMPLATES} ${PANDOC_TEX_RES} ${PANDOC_RESOURCES}/logo ${PANDOC_RESOURCES}/csl
COPY templates/classes/* ${PANDOC_TEX_RES}/.
COPY templates/pandoc/* ${PANDOC_TEMPLATES}/.
COPY templates/csl/*  ${PANDOC_RESOURCES}/csl/.
COPY templates/logo/* ${PANDOC_RESOURCES}/logo/.

# ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
ENTRYPOINT [ "/bin/bash" ]


# SCRATCH:
# ARG PANDOC_FILTERS=/root/.local/share/pandoc/filters
# COPY templates/filters/* ${PANDOC_FILTERS}/.