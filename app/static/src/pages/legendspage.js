// legendspage.js

var React = require('react');
var NavBar = require('../partials/navbar.js');
var legends = require('../legends.js');
var d3 = require('d3');
var data;

class LegendsPage extends React.Component {

	constructor() {
		super();
		this.state = {data: []};
	}

	componentDidMount() {
		// legends.getChampion(1, (err, data) => {
		// 	if (err) console.err("[LegendsPage:componentDidMount] There's been an error retrieving data!");
		// 	else this.setState({data: data});
		// })
	}

	render() {
		return (
			<div className="legends-page">
				<NavBar />
				<div className="container">
					<h3>League of Legends API Page</h3>
					<p>
						{this.state.data.name}
					</p>
				</div>
			</div>
		)
	}
}


module.exports = LegendsPage;
