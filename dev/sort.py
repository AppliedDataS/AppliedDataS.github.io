string = """
label = 'Neural Network'
fontsize = '32'
fontname = 'Arial'
node_fontname = 'Arial'
fillcolor = 'none'
fontcolor = 'Black'
style = 'filled'
fillcolor = 'none'
penwidth = '0'
pencolor = 'none'
rankdir = 'LR'
line = 'none'
splines = "line"
nodesep = '.21'
edgesep = '.002'
ranksep = "2.0"
labelloc = "t"

node_fontsize = '32'
node_fontname = 'Arial'
node_fillcolor = 'none'
node_fontcolor = 'Black'
node_style = 'filled'
node_fillcolor = 'none'
node_penwidth = '0'
node_pencolor = 'none'
node_rankdir = 'LR'
node_line = 'none'
node_splines = "line"
node_nodesep = '.21'
node_edgesep = '.002'
node_ranksep = "2.0"
node_labelloc = "t"
node_shape = 'circle'
node_style = 'filled'
node_color = 'b'
node_fillcolor ='p'
node_fontcolor = 'blue'
node_rankdir = 'TD'
node_style = 'filled'

edge_fontsize = '12'
edge_fontname = 'Arial'
edge_fillcolor = 'none'
edge_fontcolor = 'Black'
edge_style = 'filled'
edge_penwidth = '2'
edge_pencolor = 'darkgreen'
edge_rankdir = 'LR'
edge_line = 'none'
edge_splines = "line"
edge_nodesep = '.21'
edge_edgesep = '.002'
edge_ranksep = "2.0"
edge_labelloc = "t"
edge_color = 'darkviolet'
edge_arrowsize = '.5'
"""
print(sorted([x.strip() for x in string.split('\n')]))