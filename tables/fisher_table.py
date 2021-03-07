from scipy.stats import f
import numpy as np

res = """\\noindent\\begin{tabular}{*{11}{|c}|}
    \\hline
    \\diagbox{$\pmb{n_2}$}{$\pmb{n_1}$} & """
for i in range(1, 10):
    res += f"\\textbf{i} & "
res += f"\\textbf{10} \\\\ \n \\hline \n "
for n2 in range(3, 21):
    res += f"\\textbf{{{n2}}} & "
    for n1 in range(1, 10):
        q = f.ppf(1-0.05, dfn=n1, dfd=n2)
        res += f"{q:.1f} &" if q>10 else f"{q:.2f} &"
    q = f.ppf(1-0.05, dfn=10, dfd=n2)
    res += f"{q:.1f} \\\\" if q>10 else f"{q:.2f} \\\\"
    res += "\n\\hline \n"

for n2 in [22, 24, 26, 28, 30, 40, 50, 60, 100]:
    res += f"\\textbf{{{n2}}} & "
    for n1 in range(1, 10):
        q = f.ppf(1-0.05, dfn=n1, dfd=n2)
        res += f"{q:.1f} &" if q>10 else f"{q:.2f} &"
    q = f.ppf(1-0.05, dfn=10, dfd=n2)
    res += f"{q:.1f} \\\\" if q>10 else f"{q:.2f} \\\\"
    res += "\n\\hline \n"

res += "\\end{tabular}"
with open(".\\tables\\fisher_table_raw_p1.tex", "w") as fin:
    fin.write(res)

res = """\\noindent\\begin{tabular}{*{11}{|c}|}
    \\hline
    \\diagbox{$\pmb{n_2}$}{$\pmb{n_1}$} & """
for i in [12, 14, 16, 18, 20, 30, 40, 50, 60]:
    res += f"\\textbf{i} & "
res += f"\\textbf{100} \\\\ \n \\hline \n "
for n2 in range(3, 21):
    res += f"\\textbf{{{n2}}} & "
    for n1 in [12, 14, 16, 18, 20, 30, 40, 50, 60]:
        q = f.ppf(1-0.05, dfn=n1, dfd=n2)
        res += f"{q:.1f} &" if q>10 else f"{q:.2f} &"
    q = f.ppf(1-0.05, dfn=100, dfd=n2)
    res += f"{q:.1f} \\\\" if q>10 else f"{q:.2f} \\\\"
    res += "\n\\hline \n"

for n2 in [22, 24, 26, 28, 30, 40, 50, 60, 100]:
    res += f"\\textbf{{{n2}}} & "
    for n1 in [12, 14, 16, 18, 20, 30, 40, 50, 60]:
        q = f.ppf(1-0.05, dfn=n1, dfd=n2)
        res += f"{q:.1f} &" if q>10 else f"{q:.2f} &"
    q = f.ppf(1-0.05, dfn=100, dfd=n2)
    res += f"{q:.1f} \\\\" if q>10 else f"{q:.2f} \\\\"
    res += "\n\\hline \n"

res += "\\end{tabular}"
with open(".\\tables\\fisher_table_raw_p2.tex", "w") as fin:
    fin.write(res)