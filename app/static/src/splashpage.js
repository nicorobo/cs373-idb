// splash.js

var React = require('react');
var NavBar = require('./navbar.js');

class Splash extends React.Component {
	render() {
		return (
			<div className="splash-page">
				<NavBar />
				<div className="container">
					<h1>Splash</h1>
				</div>
			</div>
		)
	}
}

module.exports = Splash;


