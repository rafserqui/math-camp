import matplotlib
import matplotlib.pyplot as plt

pgf_with_custom_preamble = {
    "font.family": "serif",  # use serif/main font for text elements
    "font.serif": "Palatino",
    "text.usetex": True,    # use inline math for ticks
    "pgf.preamble":
        "\\usepackage{mathpazo} \\usepackage{gentium} \\DeclareSymbolFont{sfnumbers}{T1}{gentium}{m}{n} \\SetSymbolFont{sfnumbers}{bold}{T1}{gentium}{bx}{n} \\DeclareMathSymbol{0}\mathalpha{sfnumbers}{\"30} \\DeclareMathSymbol{1}\mathalpha{sfnumbers}{\"31} \\DeclareMathSymbol{2}\mathalpha{sfnumbers}{\"32} \\DeclareMathSymbol{3}\mathalpha{sfnumbers}{\"33} \\DeclareMathSymbol{4}\mathalpha{sfnumbers}{\"34} \\DeclareMathSymbol{5}\mathalpha{sfnumbers}{\"35} \\DeclareMathSymbol{6}\mathalpha{sfnumbers}{\"36} \\DeclareMathSymbol{7}\mathalpha{sfnumbers}{\"37} \\DeclareMathSymbol{8}\mathalpha{sfnumbers}{\"38} \\DeclareMathSymbol{9}\mathalpha{sfnumbers}{\"39} \\DeclareMathSymbol{,}\mathalpha{sfnumbers}{\"2C}"
    }
matplotlib.rcParams.update(pgf_with_custom_preamble)
import numpy as np

# Grid of parameters
rr = np.linspace(2.7, 4, 250)
T  = 1000 # Length of simulation
keep = 150 
x0 = 0.11 # Initial condition

# Function
def quadmap(x, r):
    return r * x * (1 - x)

# Initialize figure 
fig, ax = plt.subplots(figsize = (8, 6))

# Main loop over r
for q in range(len(rr)):
    r = rr[q]
    
    # Loop for simulation
    df = []
    x = x0
    for t in range(T):
        df.append(x)
        x = quadmap(x, r)
    ax.plot(r*np.ones_like(df[T-keep:]), df[T-keep:],'.g',markersize = 0.85)
ax.set_xlabel(r'$r$', fontsize = 20)
ax.set_ylabel(r'$x(t)$', fontsize = 20)
ax.set_title('Bifurcation Diagram', fontsize = 35)
plt.show()
