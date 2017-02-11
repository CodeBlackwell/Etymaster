var knex = require('../database/bookshelf').knex



knex.schema.createTableIfNotExists('latin_nouns_and_adjectives', function(table) {
    table.string('citation_form')
    table.string('declining_stem')
    table.text('english_derivatives')
    table.string('meaning')
}).then(function(){ console.log('finished creating latin_nouns_and_adjectives table') }).catch(err => { throw err })

knex.schema.createTableIfNotExists('latin_verbs', function(table) {
    table.string('citation_form')
    table.text('english_derivatives')
    table.string('participal_stem')
    table.string('perfect_stem')
    table.string('present_stem')
    table.string('meaning')
}).then(function(){ console.log('finished creating latin_verbs table') }).catch(err => { throw err })

knex.schema.createTableIfNotExists('latin_prepositions', function(table) {
    table.string('prefixes')
    table.string('word')
    table.string('meaning')
}).then(function(){ console.log('finished creating latin_prepositions table') }).catch(err => { throw err })
