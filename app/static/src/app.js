// app.js

var React = require('react');
var ReactDOM = require('react-dom');
var Navbar = require('./navbar.js');
var TablePage = require('./tablepage.js');


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
			<div className="wrapper">
				<Navbar />
				<div className="container">
					<TablePage data={characters} title="Characters"/>
				</div>
			</div>
		)
	}
}

ReactDOM.render(<App />, document.getElementById('app'))