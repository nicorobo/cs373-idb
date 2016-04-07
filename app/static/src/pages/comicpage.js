// comicpage.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var Loader = require('../partials/loader.js');
var marvel = require('../marvel.js');
var Link = require('react-router').Link;

class ComicPage extends React.Component {

	constructor() {
		super();
		this.state = {data: null};
	}

	componentDidMount() {
		marvel.getComic(this.props.params.comicId, (err, data) => {
			if (err) console.err("[ComicPage:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data.comic});
		})
	}

	render() {
		var data = this.state.data
		console.log(this.state.data);
		if (data){
			return (
				<div className="comic-page">
					<NavBar />
					<div className="container">
						<div className="row">
							<div className="col-sm-4 thumbnail-wrapper">
								<img src={data.thumbnail} />
							</div>
							<div className="col-sm-6">
								<h2>{data.title} <small>{data.id}</small></h2>
								<p>{data.description}</p>
								<ul className="fact-list">
									<li>Issue: {data.issue_num}</li>
									<li>Pages: {data.page_count}</li>
									<li>Stories: {data.number_of_stories}</li>
								</ul>
							</div>
						</div>
						<div className="row">
							<div className="col-sm-6">
								<div className="panel panel-default">
									<div className="panel-heading">Characters</div>
									<div className="panel-body list-group">
										{data.characters.map( character => {
											return (<Link to={'/characters/'+character.id} className="list-group-item comic-link">{character.name}</Link>)
										})}
									</div>
								</div>
							</div>
							<div className="col-sm-6">
								<div className="panel panel-default">
									<div className="panel-heading">Creators</div>
									<div className="panel-body list-group">
										{data.creators.map( creator => {
											return (<Link to={'/creators/'+creator.id} className="list-group-item comic-link">{creator.first_name+" "+creator.last_name}</Link>)
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
				<Loader timeout={2000} />
			)
		}
	}
}

module.exports = ComicPage;


