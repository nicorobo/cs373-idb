// character-table.js

var React = require('react');
var Table = require('./table.js');
var NavBar = require('../partials/navbar.js');
var Loader = require('../partials/loader.js');
var Paginator = require('../partials/paginator.js');
var marvel = require('../marvel.js');
var LIMIT = 20;
var headers = [
	{key: "thumbnail", value: "Thumbnail"}, 
	{key: "name", value: "Name"},
	{key: "id", value: "ID"},
	{key: "number_of_comics", value: "# of Comics"},
	{key: "number_of_stories", value: "# of Stories"},
	{key: "number_of_series", value: "# of Series"}
];

class CharacterTable extends React.Component {

	constructor(props) {
		super(props);
		this.navigateToDetail = this.navigateToDetail.bind(this);
		var page = props.location.query.page || 1;
		this.state = {data: null, page: page};
	}

	navigateToDetail(id) {
		console.log("Navigating to "+this.props.route.path+'/'+id);
		this.props.history.push(this.props.route.path+'/'+id);
	}

	componentDidMount() {
		this.getData(this.state.page);
	}

	getData(page) {
		var offset = (page-1)*LIMIT;
		marvel.getCharacters(LIMIT, 0, (err, data) => {
			if (err) console.err("[TablePage:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data.characters.slice(offset, offset+LIMIT)});
		});
	}

	render() {
		if(this.state.data){
			return (
				<div className="table-page">
					<NavBar />
					<Paginator page={this.state.page} changePage={this.getData.bind(this)} />
					<div className="container">
						<h1>{this.props.route.title}</h1>
						<Table 
							content={this.state.data}
							headers={headers}
							navigate={this.navigateToDetail}
							subject="characters"
						/>
					</div>
				</div>
			)
		} else {
			return (
				<Loader timeout={2000} />
			)
		}
	}
}

module.exports = CharacterTable;


