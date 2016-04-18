// searchresults.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var Loader = require('../partials/loader.js');
var Text = require('../partials/text.js');
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
						<h3>Search Results for “{this.props.params.searchTerm}”</h3>
						<hr />
						<h4>Comics</h4>
						<div className="panel-body list-group">
							{data.comics_and.slice(0, 20).map( comic => {
								return (<Link to={'/comics/'+comic.id} className="list-group-item comic-link"><Text name={comic.title} query={this.props.params.searchTerm} /></Link>)
							})}
							{data.comics_or.slice(0, 20).map( comic => {
								return (<Link to={'/comics/'+comic.id} className="list-group-item comic-link"><Text name={comic.title} query={this.props.params.searchTerm} /></Link>)
							})}
						</div>
						<hr />
						<h4>Characters</h4>
						<div className="panel-body list-group">
							{data.characters_and.slice(0, 20).map( character => {
								return (<Link to={'/characters/'+character.id} className="list-group-item character-link"><Text name={character.name} query={this.props.params.searchTerm} /></Link>)
							})}
							{data.characters_or.slice(0, 20).map( character => {
								return (<Link to={'/characters/'+character.id} className="list-group-item character-link"><Text name={character.name} query={this.props.params.searchTerm} /></Link>)
							})}
						</div>
						<hr />
						<h4>Creators</h4>
						<div className="panel-body list-group">
							{data.creators_and.slice(0, 20).map( creator => {
								return (<Link to={'/creators/'+creator.id} className="list-group-item creator-link"><Text name={creator.first_name} query={this.props.params.searchTerm} /></Link>)
							})}
							{data.creators_or.slice(0, 20).map( creator => {
								return (<Link to={'/creators/'+creator.id} className="list-group-item creator-link"><Text name={creator.first_name} query={this.props.params.searchTerm} /></Link>)
							})}
						</div>
						<hr />
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
