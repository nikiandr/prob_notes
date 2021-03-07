from scipy.stats import chi2

q_list = [0.990, 0.975, 0.950, 0.900, 0.100, 0.050, 0.025, 0.010]
res = """\\noindent\\begin{tabular}{*{9}{|c}|}
    \\hline
    \\diagbox{$\pmb{n}$}{$\pmb{\\alpha}$} & \\textbf{0.990} & \\textbf{0.975} & \\textbf{0.950} & \\textbf{0.900} & \\textbf{0.100} & \\textbf{0.050} & \\textbf{0.025} & \\textbf{0.010}\\\\
    \\hline \n"""

for n in range(1, 31):
    res += f"\\textbf{{{n}}} & "
    for q in q_list[:-1]:
        res += f"{chi2.ppf(1-q, df=n):.2f} &"
    res += f"{chi2.ppf(1-q_list[-1], df=n):.2f} \\\\"
    res += "\n\\hline \n"

for n in [30, 40, 50, 60, 70, 80, 90, 100]:
    res += f"\\textbf{{{n}}} & "
    for q in q_list[:-1]:
        res += f"{chi2.ppf(1-q, df=n):.2f} &"
    res += f"{chi2.ppf(1-q_list[-1], df=n):.2f} \\\\"
    res += "\n\\hline \n"
res += "\\end{tabular}"
with open(".\\tables\\chi2_table_raw.tex", "w") as fin:
    fin.write(res)