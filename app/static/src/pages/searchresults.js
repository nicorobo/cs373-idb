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
		this.setSearchData(this.props.params.searchTerm);
	}

	componentWillReceiveProps(props) {
		this.setState({data: null, loading: true});
		this.setSearchData(props.params.searchTerm);
	}

	setSearchData(searchTerm) {
		marvel.search(searchTerm, (err, data) => {
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
						<h4>Comics (AND results)</h4>
						<div className="panel-body list-group">
							{data.comics_and.slice(0, 20).map( comic => {
								return (<Link to={'/comics/'+comic.id} className="list-group-item comic-link">
										<Text name={String(comic.id)} query={this.props.params.searchTerm} attr="ID"/>
										<Text name={comic.title} query={this.props.params.searchTerm} attr="Title"/>
										<Text name={comic.description} query={this.props.params.searchTerm} attr="Description"/>
										<Text name={String(comic.page_count)} query={this.props.params.searchTerm} attr="Page Count"/>
										<Text name={String(comic.number_of_creators)} query={this.props.params.searchTerm} attr="Number of Creators"/>
										<Text name={String(comic.number_of_characters)} query={this.props.params.searchTerm} attr="Number of Characters"/>
										<Text name={String(comic.number_of_stories)} query={this.props.params.searchTerm} attr="Number of Stories"/>
										</Link>)
							})}
						</div>
						<hr />
						<h4>Characters (AND results)</h4>
						<div className="panel-body list-group">
							{data.characters_and.slice(0, 20).map( character => {
								return (<Link to={'/characters/'+character.id} className="list-group-item character-link">
										<Text name={String(character.id)} query={this.props.params.searchTerm} attr="ID"/>
										<Text name={character.name} query={this.props.params.searchTerm} attr="Name"/>
										<Text name={character.description} query={this.props.params.searchTerm} attr="Description"/>
										<Text name={String(character.number_of_comics)} query={this.props.params.searchTerm} attr="Number of Comics"/>
										<Text name={String(character.number_of_stories)} query={this.props.params.searchTerm} attr="Number of Stories"/>
										<Text name={String(character.number_of_series)} query={this.props.params.searchTerm} attr="Number of Series"/>
										</Link>)
							})}
						</div>
						<hr />
						<h4>Creators (AND results)</h4>
						<div className="panel-body list-group">
							{data.creators_and.slice(0, 20).map( creator => {
								return (<Link to={'/creators/'+creator.id} className="list-group-item creator-link">
								<Text name={String(creator.id)} query={this.props.params.searchTerm} attr="ID"/>
								<Text name={creator.first_name+" "+creator.last_name} query={this.props.params.searchTerm} attr="Name"/>
								<Text name={String(creator.number_of_comics)} query={this.props.params.searchTerm} attr="Number of Comics"/>
								<Text name={String(creator.number_of_stories)} query={this.props.params.searchTerm} attr="Number of Stories"/>
								<Text name={String(creator.number_of_series)} query={this.props.params.searchTerm} attr="Number of Series"/>
								</Link>)
							})}
						</div>
						<hr />
						<h4>Comics (OR results)</h4>
						<div className="panel-body list-group">
							{data.comics_or.slice(0, 20).map( comic => {
								return (<Link to={'/comics/'+comic.id} className="list-group-item comic-link">
								<Text name={String(comic.id)} query={this.props.params.searchTerm} attr="ID"/>
								<Text name={comic.title} query={this.props.params.searchTerm} attr="Title"/>
								<Text name={comic.description} query={this.props.params.searchTerm} attr="Description"/>
								<Text name={String(comic.page_count)} query={this.props.params.searchTerm} attr="Page Count"/>
								<Text name={String(comic.number_of_creators)} query={this.props.params.searchTerm} attr="Number of Creators"/>
								<Text name={String(comic.number_of_characters)} query={this.props.params.searchTerm} attr="Number of Characters"/>
								<Text name={String(comic.number_of_stories)} query={this.props.params.searchTerm} attr="Number of Stories"/>
								</Link>)
							})}
						</div>
						<hr />
						<h4>Characters (OR results)</h4>
						<div className="panel-body list-group">
							{data.characters_or.slice(0, 20).map( character => {
								return (<Link to={'/characters/'+character.id} className="list-group-item character-link">
								<Text name={String(character.id)} query={this.props.params.searchTerm} attr="ID"/>
								<Text name={character.name} query={this.props.params.searchTerm} attr="Name"/>
								<Text name={character.description} query={this.props.params.searchTerm} attr="Description"/>
								<Text name={String(character.number_of_comics)} query={this.props.params.searchTerm} attr="Number of Comics"/>
								<Text name={String(character.number_of_stories)} query={this.props.params.searchTerm} attr="Number of Stories"/>
								<Text name={String(character.number_of_series)} query={this.props.params.searchTerm} attr="Number of Series"/>
								</Link>)
							})}
						</div>
						<hr />
						<h4>Creators (OR results)</h4>
						<div className="panel-body list-group">
							{data.creators_or.slice(0, 20).map( creator => {
								return (<Link to={'/creators/'+creator.id} className="list-group-item creator-link">
								<Text name={String(creator.id)} query={this.props.params.searchTerm} attr="ID"/>
								<Text name={creator.first_name+" "+creator.last_name} query={this.props.params.searchTerm} attr="Name"/>
								<Text name={String(creator.number_of_comics)} query={this.props.params.searchTerm} attr="Number of Comics"/>
								<Text name={String(creator.number_of_stories)} query={this.props.params.searchTerm} attr="Number of Stories"/>
								<Text name={String(creator.number_of_series)} query={this.props.params.searchTerm} attr="Number of Series"/>
								</Link>)
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
