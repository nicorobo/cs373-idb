// loader.js

var React = require('react');
var NavBar = require('./navbar.js');

class Loader extends React.Component {
	constructor(props) {
		super(props);
		this.state = {giveup: false}
	}

	componentDidMount() {
		var timeout = this.props.timeout || 2000;
		window.setTimeout( ()=> this.setState({giveup: true}), timeout);
	}

	render() {
		console.log('This is the loader!');
		if (this.state.giveup) {
			return (
				<div className="load-page comic-page">
					<NavBar />
					<div className="container">
						<h2>No data yet, try again later!</h2>
					</div>
				</div>
			)
		}
		else {
			return (
				<div className="load-page comic-page">
					<NavBar />
					<div className="container">
						<div className="loader">
							<h2>Loading...</h2>
							<i className="fa fa-cog fa-spin"></i>
						</div>
					</div>
				</div>
			)
		}
	}
}

module.exports = Loader;
