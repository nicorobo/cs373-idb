// headeritem.js

var React = require('react');

class HeaderItem extends React.Component {
	handleClick() {
		if (this.props.headKey !== "thumbnail") {
			console.log(this.props.headKey);
			this.props.sortContents(this.props.headKey);
		}
	}

	render() {
		var sortClass = ""
		if (this.props.sortData.key === this.props.headKey) {
			if (this.props.sortData.ascending) {
				sortClass = "sort sort-ascending"
			}  else {
				sortClass = "sort sort-descending"
			}
		}

		return (
			<th onClick={this.handleClick.bind(this)} className={sortClass}>
				{this.props.headValue}
			</th>
		)
	}
}

module.exports = HeaderItem;


