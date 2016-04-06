// tableheader.js

var React = require('react');
var HeaderItem = require('./headeritem.js');

class TableHeader extends React.Component {

	render() {
		return (
			<tr>
				{this.props.content.map(info => <HeaderItem 
					sortContents={this.props.sortContent} 
					headKey={info.key} 
					headValue={info.value} 
					sortData={this.props.sortData} />)}
			</tr>
		)
	}
}
module.exports = TableHeader;


