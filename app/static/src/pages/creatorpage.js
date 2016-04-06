// creatorpage.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var marvel = require('../marvel.js');
var Link = require('react-router').Link;
var data = require('../../mockdata.json');

class CreatorPage extends React.Component {

	constructor() {
		super();
		this.state = {data: null};
	}

	componentDidMount() {
		marvel.getCreator(this.props.params.creatorId, (err, data) => {
			console.log(data);
			if (err) console.err("[CreatorPage:componentDidMount] There's been an error retrieving data!");
			else this.setState({data: data.creator});
		})
	}

	render() {
		var data = this.state.data;
		console.log(data);
		if (data) {
			return (
				<div className="character-page">
					<NavBar />
					<div className="container">
						<div className="row">
							<div className="col-sm-4 thumbnail-wrapper">
								<img src={data.thumbnail} />
							</div>
							<div className="col-sm-6">
								<h2>{data.first_name} {data.last_name} <small>{data.id}</small></h2>
								<ul className="fact-list">
									<li>Comics: {data.number_of_comics}</li>
									<li>Series: {data.number_of_series}</li>
									<li>Stories: {data.number_of_stories}</li>
								</ul>
							</div>
						</div>
						<div className="col-sm-8 col-sm-offset-2">
							<div className="panel panel-default">
								<div className="panel-heading">Creator for </div>
								<div className="panel-body list-group">
									{data.comics.slice(0, 20).map( comic => {
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

module.exports = CreatorPage;


