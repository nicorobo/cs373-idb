// searchresults.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var Loader = require('../partials/loader.js');
var marvel = require('../marvel.js');
var Link = require('react-router').Link;

class SearchResults extends React.Component {

	constructor() {
		super();
		this.state = {data: null};
	}

	componentDidMount() {
		marvel.search(1, (err, data) => {
			if (err) console.err("[SearchResults:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data.results});
		});
	}

	render() {
		var data = this.state.data
		console.log(this.state.data);
		if (data){
			return (
				<div className="search-results">
					<NavBar />
					<div className="container">
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

module.exports = SearchResults;
