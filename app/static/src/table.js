// table.js

var React = require('react');
var TableRow = require('./tablerow.js')

class Table extends React.Component {
	render() {
		console.log(this.props);
		return (
			<table className="table"> 
				<thead>
					<tr>
						{this.props.headers.map(str => <th>{str}</th> )}
					</tr>
				</thead>
				<tbody>
					{this.props.content.map(item => <TableRow content={item} />)}
				</tbody>
			</table>
		)
	}
}

module.exports = Table;

