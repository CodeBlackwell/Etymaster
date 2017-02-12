import React, { Component } from 'react'
import Radium from 'radium'
import { connect } from 'react-redux'

import NavButton from './navigation_button'
import { home, reset } from '../../data/buttons'

import { base } from '../styles/nav_bar_styles'

class NavBar extends Component {

    render () {
        return (
            <div
                className="left-navigation-bar"
                style={ base }>
                { this._renderButtons() }
            </div>
        )
    }

    _renderButtons () {
        return [home, reset].map(button, index => {
            const { kind, text, path } = button
            return <NavButton kind={ kind } text={ text } path={ path } key={ index }/>
        })
    }
}

export default Radium(NavBar)


