from scipy.stats import t
import numpy as np

q_list = [0.050, 0.025, 0.010, 0.005]
res = """\\noindent\\begin{tabular}{*{5}{|c}|}
    \\hline
    \\diagbox{$\pmb{n}$}{$\pmb{\\alpha}$} & \\textbf{0.050} & \\textbf{0.025} & \\textbf{0.010} & \\textbf{0.005} \\\\
    \\hline \n"""

for n in range(1, 21):
    res += f"\\textbf{{{n}}} & "
    for q in q_list[:-1]:
        res += f"{t.ppf(1-q, df=n):.3f} &"
    res += f"{t.ppf(1-q_list[-1], df=n):.3f} \\\\"
    res += "\n\\hline \n"

res += "\\end{tabular} \n\n"
with open(".\\tables\\student_table_raw_p1.tex", "w") as fin:
    fin.write(res)

res = """\\noindent\\begin{tabular}{*{9}{|c}|}
    \\hline
    \\diagbox{$\pmb{n}$}{$\pmb{\\alpha}$} & \\textbf{0.050} & \\textbf{0.025} & \\textbf{0.010} & \\textbf{0.005} \\\\
    \\hline \n"""
for n in range(21, 31):
    res += f"\\textbf{{{n}}} & "
    for q in q_list[:-1]:
        res += f"{t.ppf(1-q, df=n):.3f} &"
    res += f"{t.ppf(1-q_list[-1], df=n):.3f} \\\\"
    res += "\n\\hline \n"
for n in [40, 50, 60, 70, 70, 90, 100, 120, 150]:
    res += f"\\textbf{{{n}}} & "
    for q in q_list[:-1]:
        res += f"{t.ppf(1-q, df=n):.3f} &"
    res += f"{t.ppf(1-q_list[-1], df=n):.3f} \\\\"
    res += "\n\\hline \n"

res += "$\pmb{\infty}$& "
for q in q_list[:-1]:
    res += f"{t.ppf(1-q, df=100000):.3f} &"
res += f"{t.ppf(1-q_list[-1], df=100000):.3f} \\\\"
res += "\n\\hline \n"

res += "\\end{tabular}"
with open(".\\tables\\student_table_raw_p2.tex", "w") as fin:
    fin.write(res)
