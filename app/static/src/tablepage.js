// tablepage.js

var React = require('react');
var Table = require('./table.js');

class TablePage extends React.Component {
	render() {
		return (
			<div className="table-page">
				<h1>{this.props.title}</h1>
				<Table content={this.props.data.content} headers={this.props.data.headers}/>
			</div>
		)
	}
}

module.exports = TablePage;


