// navbar.js

var React = require('react');

class NavBar extends React.Component {
	render() {
		return (
			<nav className="navbar navbar-default">
				<div className="container-fluid">
					<div className="navbar-header">
						<button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
							<span className="sr-only">Toggle navigation</span>
							<span className="icon-bar"></span>
							<span className="icon-bar"></span>
							<span className="icon-bar"></span>
						</button>
						<a className="navbar-brand" href="#">Justic SWEague</a>
					</div>
					<ul className="nav navbar-nav">
						<li className="active"><a href="#">Home <span className="sr-only">(current)</span></a></li>
						<li><a href="#">About</a></li>
					</ul>
					<div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
						<ul className="nav navbar-nav navbar-right">
							<li><a href="#">Characters</a></li>
							<li><a href="#">Comics</a></li>
							<li><a href="#">Creators</a></li>
						</ul>
					</div>
				</div>
			</nav>
		)
	}
}

module.exports = NavBar;
