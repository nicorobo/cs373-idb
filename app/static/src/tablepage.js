// tablepage.js

var React = require('react');
var Table = require('./table.js');
var NavBar = require('./navbar.js');

class TablePage extends React.Component {
	render() {
		return (
			<div className="table-page">
				<NavBar />
				<div className="container">
					<h1>{this.props.title}</h1>
					<Table content={this.props.data.content} headers={this.props.data.headers}/>
				</div>
			</div>
		)
	}
}

module.exports = TablePage;


