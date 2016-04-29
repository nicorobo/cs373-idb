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
	var radiusExtent = d3.extent(data, d => d.lp);
	var xScale = d3.scale.linear().domain(xExtent).range([0, width]);
	var yScale = d3.scale.linear().domain([0, 1]).range([height, 0]);
	var radiusScale = d3.scale.linear().domain(radiusExtent).range([3, 10]);

	var xAxis = d3.svg.axis()
		.scale(xScale)
		.ticks(5)
		.orient('bottom');
	var yAxis = d3.svg.axis()
		.scale(yScale)
		.ticks(10)
		.tickFormat(d => d*100 + '%')
		.orient('left');

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
			d3.select('#summoner-name-val').text(d.name);
			d3.select('#summoner-lp-val').text(d.lp);
			d3.select('#summoner-played-val').text(d.total_games);
			d3.select('#summoner-percent-val').text((d.win_percentage*100).toFixed(2) + '%');
			d3.selectAll('.point').classed('point-dim', true);
			d3.select('#point-'+d.id).classed('point-dim', false).classed('point-spotlight', true);
		})
		.on('mouseleave', d => {
			resetInfoValues();
			d3.selectAll('.point').classed('point-dim', false);
			d3.select('#point-'+d.id).classed('point-spotlight', false);
		})

	// Render axis
	svg.append('g').attr('id', 'x-axis').call(xAxis);
	svg.append('g').attr('id', 'y-axis').call(yAxis);

	d3.select('#x-axis')
		.attr('transform', 'translate(' + 50 + ',' + 450 + ')')
	d3.select('#y-axis')
		.attr('transform', 'translate(' + 50 + ',' + 50 + ')')

	// Render Info Box
	renderInfoBox(svg, 300, 100, 20);

	function renderInfoBox(svg, x, y, spread) {
		var info = svg.append('g')
			.attr('transform', 'translate('+x+','+y+')');
		var textIds = ['summoner-name','summoner-lp','summoner-played','summoner-percent']
		var xValues = [38, 80, 80, 90];
		for(var i in textIds) {
			renderText(info, 0, (i*spread), textIds[i], 'summoner-info summoner-label');
			renderText(info, xValues[i], (i*spread), textIds[i]+'-val', 'summoner-info summoner-value');
		}
		setInfoBox();
	}

	function renderText(svg, x, y, id, className) {
		svg.append('text')
			.attr('class', className)
			.attr('id', id)
			.attr('x', x)
			.attr('y', y)
	}

	function setInfoBox() {
		d3.select('#summoner-name').text('Name: ');
		d3.select('#summoner-lp').text('League Points: ');
		d3.select('#summoner-played').text('Games Played: ');
		d3.select('#summoner-percent').text('Win Percentage: ');
	}

	function resetInfoValues() {
		d3.select('#summoner-name-val').text('');
		d3.select('#summoner-lp-val').text('');
		d3.select('#summoner-played-val').text('');
		d3.select('#summoner-percent-val').text('');
	}

}
