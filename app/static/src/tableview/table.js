// table.js

var React = require('react');
var TableRow = require('./tablerow.js')
var CharacterRow = require('./character-row.js')
var ComicRow = require('./comic-row.js')
var CreatorRow = require('./creator-row.js')
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
			this.setState({sortBy: key, ascending: true});
		}
	}

	getRows(subject, data) {
		if (subject === "characters") {
			return data.map(item => <CharacterRow onClick={this.props.navigate} content={item} />)
		} else if (subject === "comics") {
			return data.map(item => <ComicRow onClick={this.props.navigate} content={item} />)
		} else {
			return data.map(item => <CreatorRow onClick={this.props.navigate} content={item} />)
		}
	}

	render() {
		var sortedData = sortData(this.props.content, this.state.sortBy, this.state.ascending);
		var rows = this.getRows(this.props.subject, sortedData);
		return (
			<table className="table"> 
				<thead>
					<TableHeader 
						sortContent={this.sortContent.bind(this)} 
						content={this.props.headers}
						sortData={{key: this.state.sortBy, ascending: this.state.ascending}} />
				</thead>
				<tbody>
					{rows}
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
			result = -1;
		}
		return ascending ? result : result * -1;
	})
}

module.exports = Table;


