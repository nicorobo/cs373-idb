// splash.js

var React = require('react');
var NavBar = require('./navbar.js');

class Splash extends React.Component {
	render() {
		return (
			<div className="splash-page">
				<NavBar />
				<div className="container">
					<img className="splash-image" src="/static/img/Marvel_Comics.png" />
					<p className="footer">Data provided by Marvel. @2016 Marvel</p>
				</div>
			</div>
		)
	}
}

module.exports = Splash;
