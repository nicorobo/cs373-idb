// tablerow.js

var React = require('react');

class TableRow extends React.Component {
	handleClick() {
		this.props.onClick(this.props.content.id);
	}
	render() {
		var data = objValues(this.props.content);
		return (
			<tr className="table-row" onClick={this.handleClick.bind(this)}>
				{data.map(function(info) {
					if(isNaN(info) && info.indexOf("http") >= 0){
						return <td><img src={info} /></td>
					}
					return <td>{info}</td>
				})}
			</tr>
		)
	}
}

// Returns an array of all values in an object literal.
function objValues(obj) {
	var arr = [];
	for (var val in obj) {
		arr.push(obj[val]);
	}
	return arr;
}
module.exports = TableRow;


