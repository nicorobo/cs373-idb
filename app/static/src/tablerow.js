// tablerow.js

var React = require('react');

class TableRow extends React.Component {
	handleClick() {
		this.props.onClick(this.props.content.id);
	}
	render() {
		var data = objValues(this.props.content);
		return (
			<tr onClick={this.handleClick.bind(this)}>
				{data.map(info => <td>{info}</td>)}
			</tr>
		)
	}
}

// Returns an array of all values in an object literal.
function objValues(obj) {
	var arr = [];
	for (val in obj) {
		arr.push(obj[val]);
	}
	return arr;
}
module.exports = TableRow;


