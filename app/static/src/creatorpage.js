// creatorpage.js

var React = require('react');
var NavBar = require('./navbar.js');

class CreatorPage extends React.Component {
	render() {
		console.log(this.props);
		return (
			<div className="creator-page">
				<NavBar />
				<div className="container">
					<h1>Creator</h1>
					<h2>{this.props.params.creatorId}</h2>
				</div>
			</div>
		)
	}
}

module.exports = CreatorPage;


