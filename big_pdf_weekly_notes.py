from string import Template
import json
from user_functions import *
import collections
from string import Template
import os
from os import listdir
from os.path import isfile, join
import linecache


opening = r""" \documentclass[12pt, oneside]{article}

\usepackage[letterpaper, scale=0.89, centering]{geometry}
\usepackage{fancyhdr}
\setlength{\parindent}{0em}
\setlength{\parskip}{1em}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\rfoot{\href{https://creativecommons.org/licenses/by-nc-sa/2.0/}{CC BY-NC-SA 2.0} Version \today~(\thepage)}

\usepackage{amssymb,amsmath,pifont,amsfonts,comment,enumerate,enumitem}
\usepackage{currfile,xstring,hyperref,tabularx,graphicx,wasysym}
\usepackage[labelformat=empty]{caption}
\usepackage[dvipsnames,table]{xcolor}
\usepackage{multicol,multirow,array,listings,tabularx,lastpage,textcomp,booktabs}

\lstnewenvironment{algorithm}[1][] {   
    \lstset{ mathescape=true,
        frame=tB,
        numbers=left, 
        numberstyle=\tiny,
        basicstyle=\rmfamily\scriptsize, 
        keywordstyle=\color{black}\bfseries,
        keywords={,procedure, div, for, to, input, output, return, datatype, function, in, if, else, foreach, while, begin, end, }
        numbers=left,
        xleftmargin=.04\textwidth,
        #1
    }
}
{}
\lstnewenvironment{java}[1][]
{   
    \lstset{
        language=java,
        mathescape=true,
        frame=tB,
        numbers=left, 
        numberstyle=\tiny,
        basicstyle=\ttfamily\scriptsize, 
        keywordstyle=\color{black}\bfseries,
        keywords={, int, double, for, return, if, else, while, }
        numbers=left,
        xleftmargin=.04\textwidth,
        #1
    }
}
{}

\newcommand\abs[1]{\lvert~#1~\rvert}
\newcommand{\st}{\mid}

\newcommand{\A}[0]{\texttt{A}}
\newcommand{\C}[0]{\texttt{C}}
\newcommand{\G}[0]{\texttt{G}}
\newcommand{\U}[0]{\texttt{U}}

\newcommand{\cmark}{\ding{51}}
\newcommand{\xmark}{\ding{55}}

 
\begin{document}
        
        
        """

files = "notes/lessons"

# key is week and value is activity snippets

bigPDF = opening


weekFiles = []
for entry in os.scandir(files):
    file = open(entry, 'r').readlines()
    if (len(file) > 0) and ("Week" in entry.name):
        weekFiles.append(entry.name)

weekFiles = sorted(weekFiles)
print(weekFiles)

for thefiles in weekFiles:
    file = open("notes/lessons/" + thefiles, 'r').readlines()
    for line in file:
            # print("end{document}" not in line)
            if(("\input{../../resources/lesson-head.tex}" in line) or ("end{document}" in line)):
                # bigPDF += line
                # print(line)
                num = 0
            else:
                bigPDF += line


bigPDF += "\n\end{document}"

# print(bigPDF)

bigPDF += "\n\end{document}"
resultFile = open("generated/notes/lessons/complete-week.tex", "w")
resultFile.write(bigPDF)
resultFile.close()
