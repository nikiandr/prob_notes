from scipy.special import kolmogi

alpha = [0.1, 0.05, 0.025, 0.01]
lmb = kolmogi(alpha)

res = '\\begin{tabular}{|c|c|c|c|c|}\n \\hline \n$\\alpha$ & '
for a in alpha[:-1]:
    res += f'{a} & '
res += f'{alpha[-1]} \\\\\n \\hline \n'
res += '$\\lambda_{\\alpha}$ & '

for l in lmb[:-1]:
    res += f'{l:.3f} & '
res += f'{lmb[-1]:.3f} \\\\\n \\hline \n'

res += "\\end{tabular}"

with open(".\\tables\\kolmogorov_table_raw.tex", "w") as fin:
    fin.write(res)