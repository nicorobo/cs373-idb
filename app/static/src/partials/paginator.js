// paginator.js

var React = require('react');
var Link = require('react-router').Link;

class Paginator extends React.Component {

	constructor(props) {
		super(props);
		this.state = {page: parseInt(props.currentPage)};
	}

	changePage(page) {
		this.setState({page: page});
		this.props.changePage(page);
	}

	availablePages(limit, current, last) {
		var start, end;
		var middle = Math.ceil(limit / 2);
		// console.log(`limit: ${limit} current: ${current} last: ${last} middle: ${middle}`);
		var pages = [];
		// console.log(current <= middle);
		if (last <= limit) { // Show all pages, full limit not used
			// console.log('[availablePages] Under');
			start = 1;
			end = last;
		} else if (last-current <= middle) { // Right limit
			// console.log('[availablePages] Right Limit');
			start = last-limit+1;
			end = last;
		} else if (current <= middle) { // Left limit
			// console.log('[availablePages] Left Limit');
			start = 1;
			end = limit;
		} else { // Somewhere in the middle
			// console.log('[availablePages] Middle');
			var startOffset = current-middle;
			start = startOffset+1;
			end = startOffset+limit;
		}
		// console.log(`start: ${start} end: ${end}`);
		for (var i = start; i <= end; i++) {
			pages.push(i);
		}
		// console.log(pages);
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
					return <li><a href="#" onClick={()=> this.changePage(page)}>{page}</a></li>
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
		var currentPage = this.state.page;
		var hasNext = currentPage < this.props.pageLimit;
		var nextClass = currentPage < this.props.lastPage ? '' : 'disabled';
		var previousClass = currentPage > 1 ? '' : 'disabled';
		return (
			<ul className="pagination">
				<li className={previousClass}>
					<Link 
						to={{pathname: path, query:{page: currentPage-1}}} 
						onClick={this.previousPage}>
						<span aria-hidden="true">&laquo;</span>
					</Link>
				</li>
				{pages.map(page => {
					var activeClass = page == currentPage ? 'active' : ''
					return <li className={activeClass}><Link to={{pathname: path, query:{page: page}}} onClick={()=> this.changePage(page)}>{page}</Link></li>
				})}
				<li className={nextClass}>
					<Link 
						to={{pathname: path, query:{page: currentPage+1}}} 
						onClick={this.nextPage}>
						<span aria-hidden="true">&raquo;</span>
					</Link>
				</li>
			</ul>
		)
	}

	nextPage() {
		var currentPage = this.state.page;
		if(currentPage < this.props.lastPage) {
			this.setState({page: currentPage + 1});
			this.props.changePage(currentPage + 1);
		}
	}

	previousPage() {
		var currentPage = this.state.page;
		if(currentPage > 1) {
			this.setState({page: currentPage - 1});
			this.props.changePage(currentPage - 1);
		}
	}

	render() {
		var p = this.props;
		var pageButtons;
		var pages = this.availablePages(p.pageLimit, this.state.page, p.lastPage);
		if (p.pagePath) pageButtons = this.getLinkButtons(pages, p.pagePath);
		else pageButtons = this.getButtons(pages);
		return (
			<nav className="paginator">
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
