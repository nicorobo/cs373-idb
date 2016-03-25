// tableheader.js

var React = require('react');
var HeaderItem = require('./headeritem.js');

class TableHeader extends React.Component {

	render() {
		var data = objToArr(this.props.content);
		return (
			<tr>
				{data.map(info => <HeaderItem sortContents={this.props.sortContent} headKey={info.key} headValue={info.value} />)}
			</tr>
		)
	}
}

function objToArr(obj) {
	var arr = [];
	for (var val in obj) {
		arr.push({key: val, value: obj[val]})
	}
	console.log(arr);
	return arr;
}
module.exports = TableHeader;


