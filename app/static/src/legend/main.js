var legend = require('./legend.js');
var d3 = require('d3');

// Setup our visualization
var margin = {top: 50, right: 50, bottom: 50, left: 50};
var height = 500 - margin.top - margin.bottom;
var width = 500 - margin.left - margin.right;
var svg = d3.select('.legends-page').append('svg')
	.attr('height', height + margin.top + margin.bottom)
	.attr('width', width + margin.left + margin.right)
var g = svg.append('g')
	.attr('transform', 'translate('+margin.left+','+margin.top+')');

legend.getSummoners(plotData);

function plotData(err, data) {
	data = data.summoners;
	var xExtent = d3.extent(data, function(d){ return d.total_games });
	var yExtent = d3.extent(data, function(d){ return d.win_percentage });
	var radiusExtent = d3.extent(data, function(d){ return d.lp });
	var xScale = d3.scale.linear().domain(xExtent).range([0, width]);
	var yScale = d3.scale.linear().domain(yExtent).range([0, height]);
	var radiusScale = d3.scale.linear().domain(radiusExtent).range([2, 10]);
	g.selectAll('.point')
		.data(data)
		.enter()
		.append('circle')
		.attr('class', 'point')
		.attr('r', function(d){ return radiusScale(d.lp)})
		.attr('cx', function(d){ return xScale(d.total_games) })
		.attr('cy', function(d){ return yScale(d.win_percentage) })
}
