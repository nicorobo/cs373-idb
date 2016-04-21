var React = require('react');
var Link = require('react-router').Link;

class Text extends React.Component {

    constructor(props) {
		super(props);
	}

    render() {
        var query = this.props.query;
        query = query.replace(/\)/g, '').replace(/\(/g,'');
        var split_query = query.replace(/ /g, "|")
        var regex = new RegExp("(" + split_query + ")", "gi");
        var name = this.props.name;
        if (name == null) {
            return <div></div>
        }
        var parts = name.split(regex);
        var results = []

        for (var i=0; i<parts.length; i++){
            if (parts[i] != undefined && parts[i].search(regex)===0){
                results.push(<span className="result">{parts[i]}</span>);
            } else {
                results.push(parts[i])
            }
        }

        return <div><p><span className="attr">{this.props.attr}</span>: {results}</p></div>;
    }
}

Text.propTypes = {
	name: React.PropTypes.string,
	query: React.PropTypes.string,
    attr: React.PropTypes.string
}

module.exports = Text;
