// tablepage.js

var React = require('react');
var Table = require('./table.js');
var NavBar = require('./navbar.js');



const characters = {
	content: [
		{name: "Iron Man", numberOfComics: 14},
		{name: "Storm", numberOfComics: 7},
		{name: "Hulk", numberOfComics: 19}
	], 
	headers: ["Name", "Number of Comics"]
}

class TablePage extends React.Component {
	render() {
		console.log(this.props);
		return (
			<div className="table-page">
				<NavBar />
				<div className="container">
					<h1>{this.props.title}</h1>
					<Table content={characters.content} headers={characters.headers}/>
				</div>
			</div>
		)
	}
}

module.exports = TablePage;


