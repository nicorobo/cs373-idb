// splash.js

var React = require('react');
var NavBar = require('./navbar.js');

class Splash extends React.Component {
	render() {
		return (
			<div className="splash-page">
				<NavBar />
				<div className="container">
					<img className="splash-image" src="http://orig01.deviantart.net/b22a/f/2008/291/6/0/marvel_comics_logo_by_stacalkas.jpg">
					<p className="footer">@2016 Marvel</p>
				</div>
			</div>
		)
	}
}

module.exports = Splash;
