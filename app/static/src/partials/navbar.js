// navbar.js

var React = require('react');
var Link = require('react-router').Link;

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
						<a className="navbar-brand title" href="/">Justice SWEague</a>
					</div>
					<div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
						<ul className="nav navbar-nav">
							<li><Link to="/" activeClassName="active">Home</Link></li>
							<li><a href="/about">About</a></li>
						</ul>
						<ul className="nav navbar-nav navbar-right">
							<li><Link to="/characters" activeClassName="active">Characters</Link></li>
							<li><Link to="/comics" activeClassName="active">Comics</Link></li>
							<li><Link to="/creators" activeClassName="active">Creators</Link></li>
							<li><Link to="/legends" activeClassName="active">Legends</Link></li>
						</ul>
					</div>
				</div>
			</nav>
		)
	}
}

module.exports = NavBar;
