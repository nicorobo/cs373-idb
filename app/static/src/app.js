// app.js

var React = require('react');
var ReactDOM = require('react-dom');
var router = require('react-router');

var SplashPage = require('./splashpage.js');
var TablePage = require('./tablepage.js');

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
				<Router history={browserHistory} >
					<Route path="/" component={SplashPage}/>
					<Route path="/characters" data={characters} title="Characters" component={TablePage} />
					<Route path="/comics" component={wrap(<TablePage data={characters} title="Comics"/>)} />
					<Route path="/creators" component={wrap(<TablePage data={characters} title="Creators"/>)} />
					<Route path="/characters/:charId" data={characters} title="Characters" component={TablePage} />
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