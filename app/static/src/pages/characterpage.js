// characterpage.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var marvel = require('../marvel.js');
var data = require('../../mockdata.json');

class CharacterPage extends React.Component {
	render() {
		var charData = data.details[this.props.params.charId];
		if(charData){
			return (
				<div className="character-page">
					<NavBar />
					<div className="container">
						<div className="row">
							<div className="col-sm-4 thumbnail-wrapper">
								<img src={charData.thumbnail} />
							</div>
							<div className="col-sm-6">
								<h2>{charData.name} <small>{charData.id}</small></h2>
								<p>{charData.description}</p>
								<ul className="fact-list">
									<li>Comics: {charData.numberOfComics}</li>
									<li>Series: {charData.numberOfSeries}</li>
									<li>Stories: {charData.numberOfStories}</li>
								</ul>
							</div>
						</div>
						<div className="col-sm-8 col-sm-offset-2">
							<div className="panel panel-default">
								<div className="panel-heading">Appears in </div>
								<div className="panel-body list-group">
									{charData.comics.map( comic => {
										return <a onClick={()=>this.props.history.push('comics/'+comic.id)} className="list-group-item comic-link">{comic.name}</a>
									})}
								</div>
							</div>
						</div>
					</div>
				</div>
			)
		} else {
			return (
				<div className="character-page">
					<NavBar />
					<div className="container">
						<h2>No data yet, try again later!</h2>
					</div>
				</div>
			)
		}
	}
}

module.exports = CharacterPage;


