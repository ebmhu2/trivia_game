import React, {Component} from 'react';
import '../stylesheets/Question.css';

const starArray = [5, 4, 3, 2, 1]

class Question extends Component {
    constructor() {
        super();
        this.state = {
            visibleAnswer: false
        }
    }

    flipVisibility() {
        this.setState({visibleAnswer: !this.state.visibleAnswer});
    }

    createStars() {
        let {id, question, answer, category, difficulty, rating} = this.props;

        return (
            <div className="rating">
                {starArray.map(num => (
                    <div
                        key={num}
                        onClick={() => {this.props.changeRating(this.props.id, num)}}
                        className={`star  ${rating >= num ? 'active' : ''}`}

                    />
                ))}
            </div>
        )
    }

    render() {
        const {id, question, answer, category, difficulty, rating} = this.props;
        return (
            <div className="Question-holder">
                <div className="Question">{question}</div>
                <div className="Question-status">
                    <img className="category" src={`${category}.svg`}/>
                    <div className="difficulty">Difficulty: {difficulty}</div>
                    {this.createStars()}
                    <img src="delete.png" className="delete" onClick={() => this.props.questionAction('DELETE')}/>

                </div>
                <div className="show-answer button"
                     onClick={() => this.flipVisibility()}>
                    {this.state.visibleAnswer ? 'Hide' : 'Show'} Answer
                </div>
                <div className="answer-holder">
                    <span
                        style={{"visibility": this.state.visibleAnswer ? 'visible' : 'hidden'}}>Answer: {answer}</span>
                </div>
            </div>
        );
    }
}

export default Question;
