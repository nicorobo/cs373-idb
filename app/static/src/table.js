// table.js

var React = require('react');
var TableRow = require('./tablerow.js')
var TableHeader = require('./tableheader.js')

class Table extends React.Component {
	constructor() {
		super();
		this.state = {
			sortBy: "id",
			ascending: true
		}
	}
	sortContent(key) {
		if (this.state.sortBy === key) {
			console.log('[table.js] toggling order for '+key);
			this.setState({ascending: !this.state.ascending});
		} else {
			console.log('[table.js] sorting by '+key);
			this.setState({sortBy: key});
		}
	}

	render() {
		var sortedData = sortData(this.props.content, this.state.sortBy, this.state.ascending);
		return (
			<table className="table"> 
				<thead>
					<TableHeader sortContent={this.sortContent.bind(this)} content={this.props.headers} />
				</thead>
				<tbody>
					{sortedData.map(item => <TableRow onClick={this.props.navigate} content={item} />)}
				</tbody>
			</table>
		)
	}
}

function sortData (data, sortBy, ascending) {
	return data.sort(function(a, b) {
		var result;
		if (a[sortBy] >= b[sortBy]){
			result = 1;
		} else {
			result = 1;
		}
		return ascending ? result : result * -1;
	})
}

module.exports = Table;


