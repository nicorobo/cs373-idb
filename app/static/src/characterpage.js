// characterpage.js

var React = require('react');
var NavBar = require('./navbar.js');
var data = require('../mockdata.json');

class CharacterPage extends React.Component {
	render() {
		var charData = data.details[this.props.params.charId];
		console.log(charData);
		console.log(this.props);
		return (
			<div className="character-page">
				<NavBar />
				<div className="container">
					<div className="row">
						<div className="col-sm-4">
							<img src={charData.thumbnail} />
						</div>
						<div className="col-sm-6">
							<h2>{charData.name}</h2>
							<p>{charData.description}</p>
						</div>
					</div>
				</div>
			</div>
		)
	}
}

module.exports = CharacterPage;


