// loader.js

var React = require('react');
var NavBar = require('./navbar.js');

class Loader extends React.Component {
	render() {
		console.log('This is the loader!');
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

module.exports = Loader;
