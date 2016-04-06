// comicrow.js

var React = require('react');

class ComicRow extends React.Component {
	handleClick() {
		this.props.onClick(this.props.content.id);
	}
	render() {
		var data = this.props.content;
		return (
			<tr className="table-row" onClick={this.handleClick.bind(this)}>
				<td> <img src={data.thumbnail} /> </td>
				<td> {data.title} </td>
				<td> {data.id} </td>
				<td> {data.issue_num} </td>
				<td> {data.page_count} </td>
				<td> {data.number_of_stories} </td>
			</tr>
		)
	}
}

module.exports = ComicRow;


