// Datos de ejemplo para la estructura del árbol
var treeData = {
    name: "Padre",
    children: [
      {
        name: "Hijo 1",
        children: [
          {
            name: "Nieto 1"
          },
          {
            name: "Nieto 2"
          }
        ]
      },
      {
        name: "Hijo 2"
      },
      {
        name: "Hijo 3"
      }
    ]
  };
  
  // Configuración del tamaño y margen del gráfico
  var margin = { top: 20, right: 90, bottom: 30, left: 90 };
  var width = 960 - margin.left - margin.right;
  var height = 500 - margin.top - margin.bottom;
  
  // Crea el lienzo SVG para el gráfico
  var svg = d3
    .select("#tree-container")
    .append("svg")
    .attr("width", width + margin.right + margin.left)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
  // Crea un layout de árbol
  var treemap = d3.tree().size([height, width]);
  
  // Asigna los datos al layout de árbol
  var nodes = d3.hierarchy(treeData);
  var treeLayout = treemap(nodes);
  
  // Crea los enlaces entre los nodos
  var links = treeLayout.links();
  svg
    .selectAll(".link")
    .data(links)
    .enter()
    .append("path")
    .attr("class", "link")
    .attr("d", d3.linkHorizontal()
      .x(function(d) { return d.y; })
      .y(function(d) { return d.x; }));
  
  // Crea los nodos del árbol
  var nodes = treeLayout.descendants();
  svg
    .selectAll(".node")
    .data(nodes)
    .enter()
    .append("rect")
    .attr("class", "node")
    .attr("x", function(d) { return d.y - 50; })
    .attr("y", function(d) { return d.x - 10; })
    .attr("width", 100)
    .attr("height", 20);
  
  // Etiqueta los nodos con el nombre
  svg
    .selectAll(".label")
    .data(nodes)
    .enter()
    .append("text")
    .attr("class", "label")
    .attr("x", function(d) { return})  