import scipy.integrate as integrate
from numpy import pi, sqrt, exp

def F(x):
    return 1/sqrt(2*pi) * integrate.quad(lambda t: exp(-t**2/2), 0, x)[0]

#print(f"{F(1.96):.5f}")

ncol = 10
nrow = 10
s = "% !TEX root = ../main.tex\n\n"
s += "\\noindent \\begin{tabular}" + "{|" + "c|"*(ncol) + "c|}" + "\n\\hline"
s += "\n$\\pmb{x}$ & "

for i in range(ncol-1):
    s += f"\\textbf{{ 0.0{i} }} & "
s += f"\\textbf{{ 0.0{i+1} }} \\\\ \n \\hline \n"

for j in range(nrow):
    s += f"\\textbf{{ 0.{j}0 }} & "
    for i in range(ncol-1):
        s += f"{F(round(0.1*j + 0.01*i, 2)):.5f}" + " & "
    s += f"{F(round(0.1*j + 0.01*(i+1), 2)):.5f}"
    s += "\\\\ \n\\hline\n"

for j in range(nrow):
    s += f"\\textbf{{ 1.{j}0 }} & "
    for i in range(ncol-1):
        s += f"{F(round(1 + 0.1*j + 0.01*i, 2)):.5f}" + " & "
    s += f"{F(round(1 + 0.1*j + 0.01*(i+1), 2)):.5f}"
    s += "\\\\ \n\\hline\n"

for j in range(nrow):
    s += f"\\textbf{{ 2.{j}0 }} & "
    for i in range(ncol-1):
        s += f"{F(round(2 + 0.1*j + 0.01*i, 2)):.5f}" + " & "
    s += f"{F(round(2 + 0.1*j + 0.01*(i+1), 2)):.5f}"
    s += "\\\\ \n\\hline\n"

s += "\\end{tabular} \n\n"

s += "\\noindent \\begin{tabular}" + "{|" + "c|"*(ncol) + "c|}" + "\n\\hline"
s += "\n$\\pmb{x}$ & "

for i in range(ncol-1):
    s += f"\\textbf{{ 0.0{i} }} & "
s += f"\\textbf{{ 0.0{i+1} }} \\\\ \n \\hline \n"

for j in range(nrow):
    s += f"\\textbf{{ 3.{j}0 }} & "
    for i in range(ncol-1):
        s += f"{F(round(3 + 0.1*j + 0.01*i, 2)):.5f}" + " & "
    s += f"{F(round(3 + 0.1*j + 0.01*(i+1), 2)):.5f}"
    s += "\\\\ \n\\hline\n"

for j in range(nrow):
    s += f"\\textbf{{ 4.{j}0 }} & "
    for i in range(ncol-1):
        s += f"{F(round(4 + 0.1*j + 0.01*i, 2)):.5f}" + " & "
    s += f"{F(round(4 + 0.1*j + 0.01*(i+1), 2)):.5f}"
    s += "\\\\ \n\\hline\n"

s += "\\end{tabular} \n\n"

with open(".\\prob_notes\\tables\\laplace_table.tex", "w") as fin:
    fin.write(s)