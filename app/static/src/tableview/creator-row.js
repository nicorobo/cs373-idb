// creatorrow.js

var React = require('react');

class CreatorRow extends React.Component {
	handleClick() {
		this.props.onClick(this.props.content.id);
	}
	render() {
		var data = this.props.content;
		return (
			<tr className="table-row" onClick={this.handleClick.bind(this)}>
				<td> <img src={data.thumbnail} /> </td>
				<td> {data.name} </td>
				<td> {data.id} </td>
				<td> {data.number_of_comics} </td>
				<td> {data.number_of_stories} </td>
				<td> {data.number_of_series} </td>
			</tr>
		)
	}
}

module.exports = CreatorRow;


