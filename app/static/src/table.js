// table.js

var React = require('react');
var TableRow = require('./tablerow.js')

class Table extends React.Component {
	render() {
		return (
			<table className="table"> 
				<thead>
					<tr>
						{this.props.headers.map(str => <th>{str}</th> )}
					</tr>
				</thead>
				<tbody>
					{this.props.content.map(item => <TableRow onClick={this.props.navigate} content={item} />)}
				</tbody>
			</table>
		)
	}
}

module.exports = Table;


