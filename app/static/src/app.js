// app.js

var React = require('react');
var ReactDOM = require('react-dom');
var router = require('react-router');

var SplashPage = require('./splashpage.js');
var TablePage = require('./tableview/tablepage.js');
var CharacterTable = require('./tableview/character-table.js');
var ComicTable = require('./tableview/comic-table.js');
var CreatorTable = require('./tableview/creator-table.js');
var CharacterPage = require('./pages/characterpage.js');
var ComicPage = require('./pages/comicpage.js');
var CreatorPage = require('./pages/creatorpage.js');
var SearchResults = require('./pages/searchresults.js');
var NotFound = require('./pages/notfound.js');
// var LegendsPage = require('./pages/legendspage.js');

var Router = router.Router;
var Route = router.Route;
var browserHistory = router.browserHistory;

class App extends React.Component {
	render() {
		return (
			<div>
				<Router history={browserHistory} >
					<Route path="/" component={SplashPage}/>
					<Route path="/characters" title="Characters" component={CharacterTable} />
					<Route path="/comics" title="Comics" component={ComicTable} />
					<Route path="/creators" title="Creators" component={CreatorTable} />
					<Route path="/characters/:charId" component={CharacterPage} />
					<Route path="/comics/:comicId" component={ComicPage} />
					<Route path="/creators/:creatorId" component={CreatorPage} />
					<Route path="/search/:searchTerm" component={SearchResults} />
					<Route path="*" component={NotFound} />
				</Router>
			</div>
		)
	}
}

ReactDOM.render(<App />, document.getElementById('app'))
