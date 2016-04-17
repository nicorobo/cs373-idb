// searchresults.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var Loader = require('../partials/loader.js');
var marvel = require('../marvel.js');
var Link = require('react-router').Link;

class SearchResults extends React.Component {

	constructor() {
		super();
		this.state = {data: null, loading: true};
	}

	componentDidMount() {
		marvel.search(this.props.params.searchTerm, (err, data) => {
			if (err) console.error("[ComicPage:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data});
			this.setState({loading: false});
		})
	}

	render() {
		var data = this.state.data;
		if (data){
			return (
				<div className="search-results">
					<NavBar />
					<div className="container">
						<h3>Search Results</h3>
						<div className="panel-body list-group">
							{data.comics.slice(0, 20).map( comic => {
								return (<Link to={'/comics/'+comic.id} className="list-group-item comic-link">{comic.title}</Link>)
							})}
						</div>
						<div className="panel-body list-group">
							{data.characters.slice(0, 20).map( character => {
								return (<Link to={'/characters/'+character.id} className="list-group-item character-link">{character.name}</Link>)
							})}
						</div>
						<div className="panel-body list-group">
							{data.creators.slice(0, 20).map( creator => {
								return (<Link to={'/creators/'+creator.id} className="list-group-item creator-link">{creator.first_name}</Link>)
							})}
						</div>
					</div>
				</div>
			)
		} else {
			return (
				<Loader loading={this.state.loading} />
			)
		}
	}
}

module.exports = SearchResults;
