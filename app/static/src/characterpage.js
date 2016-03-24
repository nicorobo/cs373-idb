// characterpage.js

var React = require('react');
var NavBar = require('./navbar.js');

class CharacterPage extends React.Component {
	render() {
		console.log(this.props);
		return (
			<div className="character-page">
				<NavBar />
				<div className="container">
					<h1>Character</h1>
					<h2>{this.props.params.charId}</h2>
				</div>
			</div>
		)
	}
}

module.exports = CharacterPage;


