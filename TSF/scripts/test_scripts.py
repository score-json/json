import pytest
import xml.etree.ElementTree as ET
import pydot
from trudag.dotstop.core.graph import TrustableGraph
import trudag.dotstop.core.graph.graph_factory as factory
from pathlib import Path

from capture_test_data import is_unit_test, get_metadata, clean_test_case, read_result_table, get_all_xml_files
from plot_partial_graphs import get_pydot_graph, get_subgraph, get_my_url
from clean_trudag_output import clean_line, remove_line, remove_invalid_markdown_start, clean_file

def snapshot(root: Path):
    # Return a stable, content-based snapshot of the tree
    return sorted(
        (str(p.relative_to(root)).replace("\\", "/"), p.read_bytes())
        for p in root.rglob("*")
        if p.is_file()
    )

@pytest.fixture
def ET_Element_test():
    content = """
        <testcase name="test-bjdata_cpp11" classname="test-bjdata_cpp11" time="7.59149" status="run">
		<system-out>[doctest] doctest version is "2.4.11"
[doctest] run with "--help" for options
===============================================================================
[doctest] test cases:     24 |     24 passed | 0 failed | 1 skipped
[doctest] assertions: 693860 | 693860 passed | 0 failed |
[doctest] Status: SUCCESS!
</system-out>
	</testcase>
        """
    yield ET.fromstring(content)

@pytest.fixture
def ET_Element_nontest():
    content = """
        <testcase name="download_test_data" classname="download_test_data" time="9.25104" status="run">
		<system-out>[1/1] Downloading test data from https://github.com/eclipse-score/inc_nlohmann_json (branch: json_test_data_version_3_1_0_mirror)
</system-out>
	</testcase>
        """
    yield ET.fromstring(content)

@pytest.fixture
def ET_Element_nonsense():
    content = """
        <testcase name="test-bjdata_c#11" classname="test-bjdata_cpp11" time="3.1415" status="run">
		<system-out>[doctest] doctest version is "2.4.11"
[doctest] run with "--help" for options
===============================================================================
[doctest] test cases:     7 |     4 passed | 2 failed | 1 skipped
[doctest] assertions: 1914 | 1453 passed | 461 failed |
[doctest] Status: NAJA!
</system-out>
	</testcase>
        """
    yield ET.fromstring(content)

@pytest.fixture
def mock_a_trustable_repository(tmpdir):
    repo = tmpdir.mkdir("home")
    repo.join("some_nonsense_file.md").write("Hallo Welt")
    repo.join("some_cpp_code.cpp").write("#include <iostream>\n\nint main()\{std::cout << \"Hello world\";\}")
    repo.join("Root-1.md").write("---\nlevel: 1.1\nnormative: true\n---\n\ntest")
    sd = repo.mkdir("subdir")
    sd.join("node-1.md").write("---\nlevel: 1.1\nnormative: true\n---\n\ntest")
    sd.join("node-2.md").write("---\nlevel: 1.1\nnormative: true\n---\n\ntest")
    return repo

@pytest.fixture
def trustable_graph(mock_a_trustable_repository):
    my_graph = get_pydot_graph(["Root-1","node-1","node-2"],[("Root-1","node-1"),("Root-1","node-2")])
    return TrustableGraph(my_graph,factory._load_base_items(["Root-1","node-1","node-2"],Path(mock_a_trustable_repository)))

@pytest.fixture
def trudag_output():
    return """

---

### AOU-01 ### {: .item-element .item-section class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)" .status-unreviewed}

The integrator shall report problems with nlohmann/json's implementation to the upstream nlohmann/json project whenever a problem is detected.
{: .expanded-item-element }

**Supported Requests:**

- [TA-FIXES](TA.md#ta-fixes){.item-element class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}

**Supporting Items:**

_None_

{% raw %}

**References:**

_None_

{% endraw %}

**Fallacies:**

_None_

**Graph:**

_No Historic Data Found_
"""

@pytest.fixture
def trudag_output_with_cleaned_start():
    return"""
### AOU-01 ### {: .item-element .item-section class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)" .status-unreviewed}

The integrator shall report problems with nlohmann/json's implementation to the upstream nlohmann/json project whenever a problem is detected.
{: .expanded-item-element }

**Supported Requests:**

- [TA-FIXES](TA.md#ta-fixes){.item-element class="tsf-score" style="background-color:hsl(0.0, 100%, 65%)"}

**Supporting Items:**

_None_

{% raw %}

**References:**

_None_

{% endraw %}

**Fallacies:**

_None_

**Graph:**

_No Historic Data Found_
"""

@pytest.fixture
def clean_trudag_output():
    return"""
### AOU-01 

The integrator shall report problems with nlohmann/json's implementation to the upstream nlohmann/json project whenever a problem is detected.


**Supported Requests:**

- [TA-FIXES](TA.md#ta-fixes)

**Supporting Items:**

_None_



**References:**

_None_



**Fallacies:**

_None_

**Graph:**

_No Historic Data Found_
"""

@pytest.fixture
def mock_a_trudag_report(tmp_path,trudag_output):
    root = tmp_path / "report"
    root.mkdir()
    report = root / "AOU.md"
    report.write_text(trudag_output, encoding='utf8')
    return report

@pytest.fixture
def mock_a_clean_trudag_report(tmp_path,clean_trudag_output):
    root = tmp_path / "clean_report"
    root.mkdir()
    report = root / "AOU.md"
    report.write_text(clean_trudag_output, encoding='utf8')
    return report


#####################
# below are the tests
#####################

def test_unit_test_recognition(ET_Element_test,ET_Element_nontest,ET_Element_nonsense):
    assert is_unit_test(ET_Element_test)
    assert not is_unit_test(ET_Element_nontest)
    assert not is_unit_test(ET_Element_nonsense)

def test_get_metadata(ET_Element_test):
    metadata = get_metadata(ET_Element_test)
    assert metadata.get("name") == "test-bjdata"
    assert metadata.get("standard") == "gnu++11"
    assert metadata.get("passed test cases") == 24
    assert metadata.get("failed test cases") == 0
    assert metadata.get("skipped test cases") == 1
    assert metadata.get("passed assertions") == 693860
    assert metadata.get("failed assertions") == 0

def test_get_nonsense_metadata(ET_Element_nonsense):
    metadata = get_metadata(ET_Element_nonsense)
    assert metadata.get("name") == "test-bjdata"
    assert metadata.get("standard") == "gnu++c#11"
    assert metadata.get("passed test cases") == 4
    assert metadata.get("failed test cases") == 2
    assert metadata.get("skipped test cases") == 1
    assert metadata.get("passed assertions") == 1453
    assert metadata.get("failed assertions") == 461

def test_clean_test_case():    
    name, standard = clean_test_case("Hallo_Welt")
    assert name == "Hallo"
    assert standard == "gnu++Welt"
    
    name, standard = clean_test_case("Test_super_many_underscores_and_cpp_1")
    assert name == "Test_super_many_underscores_and_cpp"
    assert standard == "gnu++1"

    name, standard = clean_test_case("Test_non_nonsensical_appendix_cpp19")
    assert name == "Test_non_nonsensical_appendix"
    assert standard == "gnu++19"

def test_read_result_table():
    result_table = """[doctest] doctest version is "2.4.11"
[doctest] run with "--help" for options
===============================================================================
[doctest] test cases:  1 |  1 passed | 0 failed | 0 skipped
[doctest] assertions: 28 | 28 passed | 0 failed |
[doctest] Status: SUCCESS!
"""
    result = read_result_table([result_table])
    assert result.get("passed test cases") == 1
    assert result.get("failed test cases") == 0
    assert result.get("skipped test cases") == 0
    assert result.get("passed assertions") == 28
    assert result.get("failed assertions") == 0

    incomplete_result_table = """[doctest] doctest version is "2.4.11"
[doctest] run with "--help" for options
===============================================================================
[doctest] test cases:  1 |  1 passed | 0 failed | 0 skipped
"""
    with pytest.raises(RuntimeError):
        result = read_result_table([incomplete_result_table])

def test_get_all_xml_files(tmpdir):
    tmpdir.mkdir("ci_test_standards_clang_artefact_libcxx_17").join("clang-17_junit.xml").write("test")
    tmpdir.mkdir("ci_test_standards_clang_artefact_libcxx_14").join("clang-14_junit.xml").write("test")
    tmpdir.mkdir("ci_cmake_options_artefact_ci_test_noglobaludls").join("noglobaludls_junit.xml").write("test")
    tmpdir.mkdir("my_dir").join("graded_Hamiltonian_mechanics.tex").write("test")
    tmpdir.join("Hallo_Welt.xml").write("Hallo")
    tmpdir.mkdir("This").mkdir("is").mkdir("quite").mkdir("the").mkdir("nested").join("test.xml").write("test")
    result = get_all_xml_files(tmpdir.strpath)
    assert tmpdir+"/ci_test_standards_clang_artefact_libcxx_17/clang-17_junit.xml" in result
    assert tmpdir+"/ci_test_standards_clang_artefact_libcxx_14/clang-14_junit.xml" in result
    assert tmpdir+"/ci_cmake_options_artefact_ci_test_noglobaludls/noglobaludls_junit.xml" in result
    assert tmpdir+"/Hallo_Welt.xml" in result
    assert tmpdir+"/This/is/quite/the/nested/test.xml" in result
    assert tmpdir+"/my_dir/graded_Hamiltonian_mechanics.tex" not in result

def test_get_pydot_graph_failure():
    with pytest.raises(RuntimeError):
        get_pydot_graph(["a"],[("a","b")])

def test_comparison_of_pydot_graphs():
    # pydot graphs can not quite so easily compared. Let me demonstrate
    graph1 = pydot.Dot("G", graph_type = "digraph")
    graph1.add_node(pydot.Node("\"a\""))
    graph1.add_node(pydot.Node("\"b\""))
    graph1.add_edge(pydot.Edge("\"a\"","\"b\""))

    graph2 = pydot.Dot("G", graph_type = "digraph")
    graph2.add_node(pydot.Node("\"a\""))
    graph2.add_node(pydot.Node("\"b\""))
    graph2.add_edge(pydot.Edge("\"a\"","\"b\""))
    
    assert graph1 != graph2
    assert graph1.to_string() == graph2.to_string()
    assert graph1.to_string() == pydot.graph_from_dot_data(graph1.to_string())[0].to_string()

def test_get_pydot_graph_success():
    expected = pydot.Dot("G", graph_type = "digraph")
    # for some weird reason, Codethink expects quotation marks
    expected.add_node(pydot.Node("\"a\""))
    expected.add_node(pydot.Node("\"b\""))
    expected.add_edge(pydot.Edge("\"a\"","\"b\""))
    assert expected.to_string() == get_pydot_graph(["a","b"],[("a","b")])._graph.to_string()

def test_get_subgraph(trustable_graph):
    result = get_subgraph(trustable_graph,["Root-1"])
    expected = "digraph G {\n\"Root-1\";\n}\n"
    assert result._graph.to_string() == expected
    result = get_subgraph(trustable_graph,["Root-1","node-1"])
    expected = "digraph G {\n\"Root-1\";\n\"node-1\";\n\"Root-1\" -> \"node-1\";\n}\n"
    assert result._graph.to_string() == expected

def test_get_my_url(trustable_graph):
    assert get_my_url("Hallo","test",trustable_graph) == "test/_images/custom_Hallo_graph.svg"    
    assert get_my_url("Root-1","test",trustable_graph) == "test/_images/custom_Root-1_graph.svg"    
    assert get_my_url("node-1","test",trustable_graph) == "test/generated/node.html#node-1"    

def test_remove_line():
    assert not remove_line("test")
    assert remove_line("\"Click to view reference\"")
    assert not remove_line("\"Click to view Reference\"")
    assert remove_line("localplugins.CPPTestReference")
    assert not remove_line("localplugins.CPPTestreference")

    r"\{class[:=][^}]*\}",           # {class:...} or {class=...} with any attributes inside
    r"\{\%[\s]*raw[\s]*\%\}",        # {% raw %}
    r"\{\%[\s]*endraw[\s]*\%\}",     # {% endraw %}
    r"#{1,3}\s*\{[^}]*\}",           # one to three # followed by {: ... }
    r"\{\.[^}]*\}",                  # {.something ... }
    r"\{ \.[^}]*\}",                 # { .something ... }
    r"\{: [^}]*\}",                  # {: ... }
    
def test_clean_line():
    assert clean_line("{class: Hallo, Welt!}") == ""
    assert clean_line("This here {class: Hallo, Welt!} and a test") == "This here  and a test"
    assert clean_line("{class= Hallo, Welt!}") == ""
    assert clean_line("This here {class= Hallo, Welt!} and a test") == "This here  and a test"
    assert clean_line("{% raw %}Hallo") == "Hallo"
    assert clean_line("{% endraw %} Welt") == " Welt"
    assert clean_line("{:test}") == "{:test}"
    assert clean_line("{: test} trailing garbage") == " trailing garbage"
    assert clean_line("#{:test}") == ""
    assert clean_line("##{:test}") == ""
    assert clean_line("###{:test}") == ""
    assert clean_line("{.interesting}") == ""
    assert clean_line("{ .interesting}") == ""
    assert clean_line("{  .interesting}") == "{  .interesting}"
    assert clean_line("{ {class: test} .interesting{: test}}") == "{  .interesting}"
    assert clean_line("{{class: test}{: test} .interesting}") == ""

def test_remove_invalid_markdown_start(trudag_output,trudag_output_with_cleaned_start):
    assert remove_invalid_markdown_start(["\t","\t","---test"]) == []
    assert remove_invalid_markdown_start(trudag_output.split('\n')) == trudag_output_with_cleaned_start.split('\n')
    assert remove_invalid_markdown_start(["","","- -- Hallo"]) == ["","","- -- Hallo"]

def test_clean_file(mock_a_trudag_report,clean_trudag_output):
    clean_file(mock_a_trudag_report)
    report = (mock_a_trudag_report).read_text(encoding="utf-8")
    assert report == clean_trudag_output


