var distance=200;
var isplay=1;
var switch_second=5000;
function senceupdate(div,_width,_height){
	// d3.select('.scene-container').
    // div.select('canvas')[0][0].setAttribute('width',_width + 'px');
    // div.select('canvas')[0][0].setAttribute('height',_height + 'px');
	div.select('canvas')
        .style('width',_width + 'px')
        .style('height', _height+'px');

    // d3.select(".chart-container")
    div.style('display', '');
}

// function transform(){
// 	if(isplay==1){
// 	  i=Math.floor(Math.random()*(nodeids.length-1));
// 	  node=nodes[i];
// 	  show_node(node);
// 	}
// }
// t=setInterval(transform, switch_second);

// function show_node(node){
// 	const distRatio = 1 + distance/Math.hypot(node.x, node.y, node.z);
// 	Graph.cameraPosition(
// 	  { x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio }, 
// 	   node,  3000 );
// }

