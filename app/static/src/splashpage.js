// splash.js

var React = require('react');
var NavBar = require('./partials/navbar.js');

class Splash extends React.Component {
	render() {
		return (
			<div className="splash-page">
				<NavBar />
				<div className="container">
					<img className="splash-image" src="/static/img/Marvel_Comics.png" />
					<div className="splash-description">
						<p>Marvel Comics is an American publisher of comic books.</p>
						<p>Find information here about Marvel characters, creators, and comics.</p>
					</div>
					<p className="footer">Data provided by Marvel. @2016 Marvel</p>
				</div>
			</div>
		)
	}
}

module.exports = Splash;
