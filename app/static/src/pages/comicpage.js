// comicpage.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var marvel = require('../marvel.js');
var Link = require('react-router').Link;
var data = require('../../mockdata.json');

class ComicPage extends React.Component {

	constructor() {
		super();
		this.state = {data: {}};
	}

	componentDidMount() {
		marvel.getComic(this.props.params.comicId, (err, data) => {
			if (err) console.err("[ComicPage:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data});
		})
	}

	render() {
		var comicData = data.details[this.props.params.comicId];
		if (comicData){
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
											return (<Link to={'/characters/'+character.id} className="list-group-item comic-link">{character.name}</Link>)
										})}
									</div>
								</div>
							</div>
							<div className="col-sm-6">
								<div className="panel panel-default">
									<div className="panel-heading">Creators</div>
									<div className="panel-body list-group">
										{comicData.creators.map( creator => {
											return (<Link to={'/creators/'+creator.id} className="list-group-item comic-link">{creator.name}<span className="role">({creator.role})</span></Link>)
										})}
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			)
		} else {
			return (
				<div className="comic-page">
					<NavBar />
					<div className="container">
						<h2>No data yet, try again later!</h2>
					</div>
				</div>
			)
		}
	}
}

module.exports = ComicPage;


