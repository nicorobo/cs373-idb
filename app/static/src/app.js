// app.js

var React = require('react');
var ReactDOM = require('react-dom');
var Navbar = require('./navbar.js');
var TablePage = require('./tablepage.js');
var router = require('react-router');

var Router = router.Router;
var Route = router.Route;
var browserHistory = router.browserHistory;


const characters = {
	content: [
		{name: "Iron Man", numberOfComics: 14},
		{name: "Storm", numberOfComics: 7},
		{name: "Hulk", numberOfComics: 19}
	], 
	headers: ["Name", "Number of Comics"]
}

class App extends React.Component {
	render() {
		return (
			<div>
				<Navbar />
				<div className="container">
					<Router history={browserHistory} >
						<Route path="/" />
						<Route path="/characters" component={wrap(<TablePage data={characters} title="Characters"/>)} />
						<Route path="/comics" component={wrap(<TablePage data={characters} title="Comics"/>)} />
						<Route path="/creators" component={wrap(<TablePage data={characters} title="Creators"/>)} />
					</Router>
				</div>
			</div>
		)
	}
}

function wrap(component) {
	return React.createClass({
		render: function() {
			return component
		}
	})
}

ReactDOM.render(<App />, document.getElementById('app'))