from prettytable import PrettyTable

t = PrettyTable(['Name', 'Age'])

t.align = 'l'
t.add_row(['Alice', 24])
t.add_row(['Bob', 19])



print t