from string import Template
import os
import linecache
from user_functions import *

#TODO: use header file ... 
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
bigPDF = opening


directoryFolder = "notes/activity-snippets"

definition_array = []
for filename in os.listdir(directoryFolder):
    # print(filename)
    if("definition" in filename):
        # print(filename)
        definition_array.append(filename)

definition_array = sorted(definition_array)

for filename in definition_array:
    weekly = open (directoryFolder+"/"+filename, "r")
        
    lines = weekly.readlines()

    strNew = ""
    for line in reversed(lines):
        if(line.startswith("%!") or line.startswith("\n")):
            lines.remove(line)
        
    strNew += opening

    for line in lines:
        strNew += line
        bigPDF += line

    bigPDF += "\n"

    strNew += "\n\end{document}"
    # print(strNew)
    
    #TODO: call write_if_different before writing here. 
    write_if_different("generated/notes/activity-snippets-flat/" + filename, strNew)
    # resultFile = open("generated/notes/activity-snippets-flat/" + filename, "w")
    # resultFile.write(strNew)
    # resultFile.close()

bigPDF += "\n\end{document}"
write_if_different("generated/notes/activity-snippets-flat/full-definition.tex", bigPDF)
# resultFile = open("generated/notes/activity-snippets-flat/full-definition.tex", "w")
# resultFile.write(bigPDF)
# resultFile.close()