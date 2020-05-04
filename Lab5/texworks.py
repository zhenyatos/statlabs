def heading(size):
    return "\hline $n=" + str(size) + "$&$r$&$r_S$&$r_Q$  \\\\"


def values(param, val):
    return "\hline" + param + \
           "&" + str(val[0]) + \
           "&" + str(val[1]) + \
           "&" + str(val[2]) + "\\\\"


def empty():
    return "\hline &  &  &  \\\\"


def tabular(str):
    return "\\begin{tabular}{|l|l|l|l|}" + str + "\hline \\end{tabular}"
