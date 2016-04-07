// paginator.js

var React = require('react');
var Link = require('react-router').Link;

class Paginator extends React.Component {
	render() {
		return (
			<nav>
				<ul className="pagination">
					<li>
						<a href="#" aria-label="Previous">
							<span aria-hidden="true">&laquo;</span>
						</a>
					</li>
					<li><Link to={{pathname: "/characters", query:{page: 1}}} onClick={()=> this.props.changePage(1)}>1</Link></li>
					<li><Link to={{pathname: "/characters", query:{page: 2}}} onClick={()=> this.props.changePage(2)}>2</Link></li>
					<li><Link to={{pathname: "/characters", query:{page: 3}}} onClick={()=> this.props.changePage(3)}>3</Link></li>
					<li><Link to={{pathname: "/characters", query:{page: 4}}} onClick={()=> this.props.changePage(4)}>4</Link></li>
					<li><Link to={{pathname: "/characters", query:{page: 5}}} onClick={()=> this.props.changePage(5)}>5</Link></li>
					<li>
						<a href="#" aria-label="Next">
							<span aria-hidden="true">&raquo;</span>
						</a>
					</li>
				</ul>
			</nav>
		)
	}
}

module.exports = Paginator;
