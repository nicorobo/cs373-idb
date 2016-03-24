// app.js

var React = require('react');
var ReactDOM = require('react-dom');
var Navbar = require('./navbar.js');
var TablePage = require('./tablepage.js');
var router = require('react-router');

var Router = router.Router;
var Route = router.Route;
var hashHistory = router.hashHistory;


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
				<Router history={hashHistory}>
					<Route path="/" component={wrap(<TablePage data={characters} title="Characters"/>)} />
				</Router>
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