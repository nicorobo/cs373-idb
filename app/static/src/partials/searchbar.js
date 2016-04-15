var React = require('react');
var Link = require('react-router').Link;
var marvel = require('../marvel.js');
var searchTerm;

class SearchBar extends React.Component {
    constructor() {
        super();
        this.state = {searchTerm: ""}
    }

    handleChange(event) {
        this.setState({searchTerm: event.target.value})
    }

	render() {
		return (
            <span>
    			<form className="searchForm">
    				<input type="text" placeholder="Search" onChange={this.handleChange.bind(this)} />
    			</form>
                <Link to={'/search/'+this.state.searchTerm} className="searchButton">Go</Link>
            </span>
		)
	}
}

module.exports = SearchBar;
