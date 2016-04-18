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

    handleKeyDown(event) {
        // If return key is pressed, commence search
        if(event.keyCode === 13) {
            document.getElementById('searchButton').click();
        }
    }

	render() {
		return (
            <span>
    			<form className="searchForm">
    				<input type="text" placeholder="Search" onKeyDown={this.handleKeyDown.bind(this)} onChange={this.handleChange.bind(this)} />
    			</form>
                <Link id="searchButton" to={'/search/'+this.state.searchTerm} className="searchButton">Go</Link>
            </span>
		)
	}
}

module.exports = SearchBar;
