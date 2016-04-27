var legend = require('./legend.js');
var d3 = require('d3');
var store = require('store');


// Setup our visualization
var margin = {top: 50, right: 50, bottom: 50, left: 50};
var height = 500 - margin.top - margin.bottom;
var width = 500 - margin.left - margin.right;
var svg = d3.select('.legends-page').append('svg')
	.attr('height', height + margin.top + margin.bottom)
	.attr('width', width + margin.left + margin.right)
var g = svg.append('g')
	.attr('transform', 'translate('+margin.left+','+margin.top+')');

// Cacheing data so it doesn't take so long to load
if(!store.enabled) {
	legend.getSummoners(plotData);
} else {
	if(store.get('legendData')) {
		plotData(null, store.get('legendData'));
	} else {
		legend.getSummoners((err, data) => {
			store.set('legendData', data);
			plotData(err, data);
		})
	}
}

function plotData(err, data) {
	data = data.summoners || data;
	var xExtent = d3.extent(data, d => d.total_games);
	var yExtent = d3.extent(data, d => d.win_percentage);
	console.log(xExtent);
	var radiusExtent = d3.extent(data, d => d.lp);
	var xScale = d3.scale.linear().domain(xExtent).range([0, width]);
	var yScale = d3.scale.linear().domain(yExtent).range([height, 0]);
	var radiusScale = d3.scale.linear().domain(radiusExtent).range([2, 10]);

	var xAxis = d3.svg.axis().scale(xScale).ticks(5).orient('bottom');
	var yAxis = d3.svg.axis().scale(yScale).ticks(5).orient('left');

	// Render points
	g.selectAll('.point')
		.data(data)
		.enter()
		.append('circle')
		.attr('class', 'point')
		.attr('id', d => 'point-'+d.id)
		.attr('r', d => radiusScale(d.lp))
		.attr('cx', d => xScale(d.total_games))
		.attr('cy', d => yScale(d.win_percentage))
		.on('mouseover', d => {
			d3.selectAll('.point').classed('point-dim', true);
			d3.select('#point-'+d.id).classed('point-dim', false).classed('point-spotlight', true);
		})
		.on('mouseleave', d => {
			d3.selectAll('.point').classed('point-dim', false);
			d3.select('#point-'+d.id).classed('point-spotlight', false);
		})

	// Render axis
	svg.append('g').attr('id', 'x-axis').call(xAxis);
	svg.append('g').attr('id', 'y-axis').call(yAxis);
	d3.select('#x-axis')
		.attr('transform', 'translate(' + 50 + ',' + 450 + ')')
		// .selectAll('text').attr('x', '50')
	d3.select('#y-axis')
		.attr('transform', 'translate(' + 50 + ',' + 50 + ')')
		// .selectAll('text').attr('x', '50')

}
