"use strict"
const knex = require('../database/bookshelf').knex
const bookshelf = require('../database/bookshelf').bookshelf
const Latin = require('../database/latin_tables.json')

const { nouns_and_adjectives, verbs, prepositions} = Latin

const Latin_nouns_and_adjectives = bookshelf.Model.extend({
    tableName: 'latin_nouns_and_adjectives'
});

const Latin_verbs = bookshelf.Model.extend({
    tableName: 'latin_verbs'
});

const Latin_prepositions = bookshelf.Model.extend({
    tableName: 'latin_prepositions'
})


knex('latin_nouns_and_adjectives').insert(nouns_and_adjectives)
    .then(() => console.log('insertion complete. Enjoy your data!'))
.catch(error => { throw error })

knex('latin_verbs').insert(verbs)
    .then(() => console.log('insertion complete. Enjoy your data!'))
.catch(error => { throw error })

knex('latin_prepositions').insert(prepositions)
    .then(() => console.log('insertion complete. Enjoy your data!'))
.catch(error => { throw error })
