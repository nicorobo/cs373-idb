// comicpage.js

var React = require('react');
var NavBar = require('./navbar.js');
var data = require('../mockdata.json');

class ComicPage extends React.Component {
	render() {
		var comicData = data.details[this.props.params.comicId];
		console.log(comicData);
		console.log(this.props);
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
	}
}

module.exports = ComicPage;


