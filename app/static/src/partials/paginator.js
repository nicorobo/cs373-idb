// paginator.js

var React = require('react');
var Link = require('react-router').Link;

class Paginator extends React.Component {
	constructor(props) {
		super(props);
		this.state = {page: parseInt(props.currentPage)};
	}

	availablePages(limit, current, last) {
		var start, end;
		var middle = Math.ceil(limit / 2);
		console.log(`limit: ${limit} current: ${current} last: ${last} middle: ${middle}`);
		var pages = [];
		console.log(current <= middle);
		if (last <= limit) { // Show all pages, full limit not used
			console.log('[availablePages] Under');
			start = 1;
			end = last;
		} else if (last-current <= middle) { // Right limit
			console.log('[availablePages] Right Limit');
			start = last-limit+1;
			end = last;
		} else if (current <= middle) { // Left limit
			console.log('[availablePages] Left Limit');
			start = 1;
			end = limit;
		} else { // Somewhere in the middle
			console.log('[availablePages] Middle');
			var startOffset = current-middle;
			start = startOffset+1;
			end = startOffset+limit;
		}
		console.log(`start: ${start} end: ${end}`);
		for (var i = start; i <= end; i++) {
			pages.push(i);
		}
		console.log(pages);
		return pages;
	}

	getButtons(pages) {
		return (
			<ul className="pagination">
				<li>
					<a href="#" aria-label="Previous">
						<span aria-hidden="true">&laquo;</span>
					</a>
				</li>
				{pages.map(page => {
					return <li><a href="#" onClick={()=> this.props.changePage(page)}>{page}</a></li>
				})}
				<li>
					<a href="#" aria-label="Next">
						<span aria-hidden="true">&raquo;</span>
					</a>
				</li>
			</ul>
		)
	}

	getLinkButtons(pages, path) {
		return (
			<ul className="pagination">
				<li>
					<a href="#" aria-label="Previous">
						<span aria-hidden="true">&laquo;</span>
					</a>
				</li>
				{pages.map(page => {
					return <li><Link to={{pathname: path, query:{page: page}}} onClick={()=> this.props.changePage(page)}>{page}</Link></li>
				})}
				<li>
					<a href="#" aria-label="Next">
						<span aria-hidden="true">&raquo;</span>
					</a>
				</li>
			</ul>
		)
	}

	nextPage() {

	}

	previousPage() {

	}

	render() {
		var p = this.props;
		var pageButtons;
		var pages = this.availablePages(p.pageLimit, p.currentPage, p.lastPage);
		if (p.pagePath) pageButtons = this.getLinkButtons(pages, p.pagePath);
		else pageButtons = this.getButtons(pages);
		return (
			<nav>
				{pageButtons}
			</nav>
		)
	}
}

Paginator.propTypes = {
	currentPage: React.PropTypes.number,
	changePage: React.PropTypes.func,
	pagePath: React.PropTypes.string,
	lastPage: React.PropTypes.number,
	pageLimit: React.PropTypes.number,
}
Paginator.defaultProps = {
	currentPage: 1,
	lastPage: 10,
	pageLimit: 5,
}

module.exports = Paginator;
