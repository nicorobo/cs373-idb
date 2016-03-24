// chomicpage.js

var React = require('react');
var NavBar = require('./navbar.js');
var data = require('../mockdata.json');

class ComicPage extends React.Component {
	render() {
		console.log(this.props);
		return (
			<div className="comic-page">
				<NavBar />
				<div className="container">
					<h1>Comic</h1>
					<h2>{this.props.params.comicId}</h2>
				</div>
			</div>
		)
	}
}

module.exports = ComicPage;


