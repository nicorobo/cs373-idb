
// comic-table.js

var React = require('react');
var Table = require('./table.js');
var NavBar = require('../partials/navbar.js');
var Loader = require('../partials/loader.js');
var marvel = require('../marvel.js');
var headers = [
	{key: "thumbnail", value: "Thumbnail"},
	{key: "title", value: "Title"},
	{key: "id", value: "ID"},
	{key: "issue_num", value: "Issue"},
	{key: "page_count", value: "Pages"},
	{key: "number_of_stories", value: "# of Stories"}
];

class ComicTable extends React.Component {

	constructor() {
		super();
		this.navigateToDetail = this.navigateToDetail.bind(this);
		this.state = {data: null};
	}

	navigateToDetail(id) {
		console.log("Navigating to "+this.props.route.path+'/'+id);
		this.props.history.push(this.props.route.path+'/'+id);
	}

	componentDidMount() {
		marvel.getComics(20, 0, (err, data) => {
			if (err) console.err("[TablePage:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data.comics.slice(0, 20)});
		});
	}

	render() {
		if(this.state.data){
			return (
				<div className="table-page">
					<NavBar />
					<div className="container">
						<h1>{this.props.route.title}</h1>
						<Table 
							content={this.state.data} 
							headers={headers} 
							navigate={this.navigateToDetail}
							subject="comics"
						/>
					</div>
				</div>
			)
		} else {
			return (
				<Loader timeout={8000} />
			)
		}
	}
}

module.exports = ComicTable;


