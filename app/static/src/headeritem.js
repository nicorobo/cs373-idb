// headeritem.js

var React = require('react');

class HeaderItem extends React.Component {
	handleClick() {
		this.props.sortContents(this.props.headKey);
	}
	render() {
		return (
			<th onClick={this.handleClick.bind(this)}>
				{this.props.headValue}
			</th>
		)
	}
}

module.exports = HeaderItem;


