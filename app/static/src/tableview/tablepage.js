// tablepage.js

var React = require('react');
var Table = require('./table.js');
var NavBar = require('../partials/navbar.js');
var library = require('../mockdata.json');
var data;

class TablePage extends React.Component {

	constructor() {
		super();
		this.navigateToDetail = this.navigateToDetail.bind(this);
	}

	navigateToDetail(id) {
		console.log("Navigating to "+this.props.route.path+'/'+id);
		this.props.history.push(this.props.route.path+'/'+id);
	}

	render() {

		if (this.props.route.path === '/characters') data = library.characters;
		else if (this.props.route.path === '/comics') data = library.comics;
		else data = library.creators;

		console.log(library);

		return (
			<div className="table-page">
				<NavBar />
				<div className="container">
					<h1>{this.props.route.title}</h1>
					<Table content={data.content} headers={data.headers} navigate={this.navigateToDetail}/>
				</div>
			</div>
		)
	}
}

module.exports = TablePage;


