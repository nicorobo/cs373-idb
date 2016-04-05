// app.js

var React = require('react');
var ReactDOM = require('react-dom');
var router = require('react-router');

var SplashPage = require('./splashpage.js');
var TablePage = require('./tableview/tablepage.js');
var CharacterPage = require('./pages/characterpage.js');
var ComicPage = require('./pages/comicpage.js');
var CreatorPage = require('./pages/creatorpage.js');

var Router = router.Router;
var Route = router.Route;
var browserHistory = router.browserHistory;

class App extends React.Component {
	render() {
		return (
			<div>
				<Router history={browserHistory} >
					<Route path="/" component={SplashPage}/>
					<Route path="/characters" title="Characters" component={TablePage} />
					<Route path="/comics" title="Comics" component={TablePage} />
					<Route path="/creators" title="Creators" component={TablePage} />
					<Route path="/characters/:charId" component={CharacterPage} />
					<Route path="/comics/:comicId" component={ComicPage} />
					<Route path="/creators/:creatorId" component={CreatorPage} />
				</Router>
			</div>
		)
	}
}

ReactDOM.render(<App />, document.getElementById('app'))