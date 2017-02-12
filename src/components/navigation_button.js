import React, { Component, PropTypes } from 'react';
import { Link } from 'react-router';
import Radium from 'radium';

import styles from '../styles/nav_button_styles'



class NavigationButton extends Component {
    // static propTypes = {
    //     kind: PropTypes.oneOf(['primary', 'reset']).isRequired,
    //     path: PropTypes.string.isRequired,
    //     text: PropTypes.string.isRequired
    // }

    render () {
        const {
            path,
            text,
            kind
        } = this.props

        const {
            base
        } = styles

        return (
            <div className="nav-button" >
                <Link to={ path } style={[ base, styles[kind] ]}>
                     { text }
                </Link>
            </div>
        )
    }
}

export default Radium(NavigationButton)
