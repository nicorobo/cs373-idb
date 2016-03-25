// comicpage.js

var React = require('react');
var NavBar = require('./navbar.js');
var data = require('../mockdata.json');

class ComicPage extends React.Component {
	render() {
		var comicData = data.details[this.props.params.comicId];
		console.log(comicData);
		return (
			<div className="comic-page">
				<NavBar />
				<div className="container">
					<div className="row">
						<div className="col-sm-4 thumbnail-wrapper">
							<img src={comicData.thumbnail} />
						</div>
						<div className="col-sm-6">
							<h2>{comicData.title} <small>{comicData.id}</small></h2>
							<p>{comicData.description}</p>
							<ul className="fact-list">
								<li>Issue: {comicData.issue}</li>
								<li>Pages: {comicData.pageCount}</li>
								<li>Stories: {comicData.numberOfStories}</li>
							</ul>
						</div>
					</div>
					<div className="row">
						<div className="col-sm-6">
							<div className="panel panel-default">
								<div className="panel-heading">Characters</div>
								<div className="panel-body list-group">
									{comicData.characters.map( character => {
										return <a onClick={()=>this.props.history.push('characters/'+character.id)} className="list-group-item comic-link">{character.name}</a>
									})}
								</div>
							</div>
						</div>
						<div className="col-sm-6">
							<div className="panel panel-default">
								<div className="panel-heading">Creators</div>
								<div className="panel-body list-group">
									{comicData.creators.map( creator => {
										return <a onClick={()=>this.props.history.push('creators/'+creator.id)} className="list-group-item comic-link">{creator.name}<span className="role">({creator.role})</span></a>
									})}
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		)
	}
}

module.exports = ComicPage;


