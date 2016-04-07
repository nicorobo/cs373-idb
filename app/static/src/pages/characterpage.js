// characterpage.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var Loader = require('../partials/loader.js');
var marvel = require('../marvel.js');
var Link = require('react-router').Link;

class CharacterPage extends React.Component {

	constructor() {
		super();
		this.state = {data: null};
	}

	componentDidMount() {
		marvel.getCharacter(this.props.params.charId, (err, data) => {
			if (err) console.err("[CharacterPage:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data.character});
		})
	}

	render() {
		var data = this.state.data;
		console.log(data);
		if(data){
			return (
				<div className="character-page">
					<NavBar />
					<div className="container">
						<div className="row">
							<div className="col-sm-4 thumbnail-wrapper">
								<img src={data.thumbnail} />
							</div>
							<div className="col-sm-6">
								<h2>{data.name} <small>{data.id}</small></h2>
								<p>{data.description}</p>
								<ul className="fact-list">
									<li>Comics: {data.number_of_comics}</li>
									<li>Series: {data.number_of_series}</li>
									<li>Stories: {data.number_of_stories}</li>
								</ul>
							</div>
						</div>
						<div className="col-sm-8 col-sm-offset-2">
							<div className="panel panel-default">
								<div className="oreo panel-heading">Appears in </div>
								<div className="panel-body list-group">
									{data.comics.slice(0,20).map( comic => {
										return (<Link to={'/comics/'+comic.id} className="list-group-item comic-link">{comic.title}</Link>)

									})}
								</div>
							</div>
						</div>
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

module.exports = CharacterPage;


