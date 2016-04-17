// loader.js

var React = require('react');
var NavBar = require('./navbar.js');
var timeid;
class Loader extends React.Component {
	render() {
		if (!this.props.loading) {
			return (
				<div className="load-page comic-page">
					<NavBar />
					<div className="container">
						<h2>No data yet, try again later!</h2>
					</div>
				</div>
			)
		}
		else {
			return (
				<div className="load-page comic-page">
					<NavBar />
					<div className="container">
						<div className="loader">
							<h2>Loading...</h2>
							<i className="fa fa-cog fa-spin"></i>
						</div>
					</div>
				</div>
			)
		}
	}
}

module.exports = Loader;
