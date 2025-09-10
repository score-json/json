import sys
import pydot
import graphviz as gz
from trudag.dotstop.core.graph import TrustableGraph, PydotGraph
import trudag.dotstop.core.graph.graph_factory as factory
import trudag.plot as plt
from pathlib import Path

def get_my_url(vertex: str, base_url: str, fuLl_graph: TrustableGraph) -> str:
    # if vertex in fuLl_graph._graph.root_nodes():
    #     return base_url+"_images/graph.svg"
    if vertex in fuLl_graph._graph.leaf_nodes():
        return base_url+"/generated/"+fuLl_graph.get_item(vertex).document+".html#"+vertex.lower()
    else:
        return base_url+"/_images/"+vertex+".svg"

def get_pydot_graph(vertices: list[str], edges: list[tuple[str,str]]) -> PydotGraph:
    graph = "digraph G {"
    for vertex in vertices:
        graph += f"\"{vertex}\";"
    for source, target in edges:
        graph += f"\"{source}\" -> \"{target}\";"
    graph += "}"
    return PydotGraph.from_string(graph)

def get_subgraph(full_graph: TrustableGraph, vertices: list[str]) -> TrustableGraph:
    edges = [(src,dst) for src, dst in full_graph._graph.edges() if src in vertices and dst in vertices]
    graph = get_pydot_graph(vertices,edges)
    nodes = [full_graph.get_item(vertex) for vertex in vertices]
    return TrustableGraph(graph,nodes)

def plot_all_single_layer_subgraphs(full_graph: TrustableGraph, path: list[str], base_url: str = "") -> list[tuple[str,int]]:
    result = []
    bud = path[-1]
    new_children = full_graph._graph.successors(bud)
    vertices = path+new_children
    my_graph = get_subgraph(full_graph,vertices)
    if len(new_children) > 0:
        plot_blank(my_graph,full_graph,base_url,"./TSF/docs/generated/"+bud+".svg")
        result.append([bud,len(path)])
        for child in new_children:
            new_path = path + [child]
            result = result + plot_all_single_layer_subgraphs(full_graph,new_path,base_url)
    return result

def write_documentation(plots: list[tuple[str,int]]):
    sorted_plots = sorted(plots, key=lambda x: x[1])
    for bud, length in sorted_plots:
        with open("./TSF/docs/trustable_graph.rst", "a", encoding="utf-8") as documentation:
            documentation.write("\n\n.. image:: generated/"+bud+".svg\n")
            documentation.write("\t:alt: Root of the trustable graph\n\t:width: 6000px\n\n")
            documentation.write("Trustable graph centered at "+bud)

def plot_blank(graph: TrustableGraph, full_graph: TrustableGraph, base_url = "", name = "./graph.svg"):
    # format trustable graph for plotting purposes
    formatted_graph = pydot.graph_from_dot_data(str(graph))[0]
    formatted_graph.set("rankdir", "TB")
    formatted_graph.set("newrank", "true")
    # increase vertical distance between the nodes for improved viewing experience
    formatted_graph.set("ranksep", "2.0")

    # Remove edge and node sha's, required to support some plantuml servers.
    for element in formatted_graph.get_nodes() + formatted_graph.get_edges():
        if "sha" in element.get_attributes():
            element.get_attributes().pop("sha")

    for item in graph.items:
        # remove non-normative-nodes
        if not item.normative:
            formatted_graph.del_node(pydot.quote_id_if_necessary(str(item)))
        else:
            formatted_node = formatted_graph.get_node(
                pydot.quote_id_if_necessary(str(item))
            )[0]
            formatted_node.set("label", plt.break_line_at(item.header(), 20))
            formatted_node.set("URL", get_my_url(str(item),base_url,full_graph))
            # Set target to avoid URLs opening within the image
            # formatted_node.set("target", "_top")
            for key, value in plt.NODE_STYLE.items():
                formatted_node.set(key, value)

    dot_source = gz.Source(formatted_graph.to_string())
    dot_source.format = 'svg'
    dot_source.render(Path(name).with_suffix(""))

def plot_orchestrator(full_graph: TrustableGraph, base_url: str = ""):
    # initialise the documentation
    documentation_content = """
.. _ta-analysis-subgraph:

Trustable Graph
====================

The trustable graph is the graphical representation of the argumentation.

.. image:: generated/graph.svg
   :alt: Trustable Graph
   :width: 6000px

This image presents the full trustable graph, in which each item links to its entry in the documentation. Smaller scale representations of arguments, which are navigable among each other, can be found below. 
    """
    with open("./TSF/docs/trustable_graph.rst", "a", encoding="utf-8") as documentation:
        documentation.write(documentation_content)
    roots = full_graph._graph.root_nodes()
    leafs = full_graph._graph.leaf_nodes()
    for root in roots:
        # if the root is an orphaned node, discard it
        if root in leafs:
            continue
        write_documentation(plot_all_single_layer_subgraphs(full_graph,[root],base_url))
        

# prepare the trustable graph as in trudag.plot.format_source_from_graph

# build trustable graph from .dotstop.dot
full_trustable_graph = factory.build_trustable_graph(Path('.dotstop.dot'),Path('.'))

plot_orchestrator(full_trustable_graph,sys.argv[1])