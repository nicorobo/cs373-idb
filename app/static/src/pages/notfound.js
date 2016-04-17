// notfound.js

var React = require('react');
var NavBar = require('../partials/navbar.js');

class NotFound extends React.Component {
	render() {
		return (
			<div className="not-found-page">
				<NavBar />
				<div className="container">
					<h2>Sorry, Page Not Found </h2>
				</div>
			</div>
		)
	}
}

module.exports = NotFound;
