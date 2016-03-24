// app.js

var React = require('react');
var ReactDOM = require('react-dom');
var router = require('react-router');

var SplashPage = require('./splashpage.js');
var TablePage = require('./tablepage.js');
var CharacterPage = require('./characterpage.js');
var ComicPage = require('./comicpage.js');
var CreatorPage = require('./creatorpage.js');

var Router = router.Router;
var Route = router.Route;
var browserHistory = router.browserHistory;

class App extends React.Component {
	render() {
		return (
			<div>
				<Router history={browserHistory} >
					<Route path="/" component={SplashPage}/>
					<Route path="/characters" component={TablePage} />
					<Route path="/comics" component={wrap(<TablePage title="Comics"/>)} />
					<Route path="/creators" component={wrap(<TablePage title="Creators"/>)} />
					<Route path="/characters/:charId" component={CharacterPage} />
					<Route path="/comics/:comicId" component={ComicPage} />
					<Route path="/creators/:creatorId" component={CreatorPage} />
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