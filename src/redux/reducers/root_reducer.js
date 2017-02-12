import { combineReducers } from 'redux'
import homepage from './homepage_reducer'
import navigation from './navigation_reducer'
import { routerReducer } from 'react-router-redux'

export default combineReducers({
    homepage,
    navigation,
    routing: routerReducer
});
