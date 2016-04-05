// tablepage.js

var React = require('react');
var Table = require('./table.js');
var NavBar = require('../partials/navbar.js');
var library = require('../../mockdata.json');
var data;

class TablePage extends React.Component {

	constructor() {
		super();
		this.navigateToDetail = this.navigateToDetail.bind(this);
		this.state = {data: []};
	}

	navigateToDetail(id) {
		console.log("Navigating to "+this.props.route.path+'/'+id);
		this.props.history.push(this.props.route.path+'/'+id);
	}

	componentDidMount() {
		var populate;
		if (this.props.route.path === '/characters') populate = marvel.getCharacters;
		else if (this.props.route.path === '/comics') populate = marvel.getComics;
		else populate = marvel.getCreators;
		populate(20, 0, (err, data) => {
			if (err) console.err("[TablePage:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data});
		});
	}

	render() {

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


