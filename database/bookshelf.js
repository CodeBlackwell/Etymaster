var knex = require('knex')({
    client:           'pg',
    connection:       {
        host:     process.env.DATABASE_URL,
        user:     process.env.DATABASE_USER,
        password: process.env.DATABASE_PASSWORD,
        database: 'etymaster',
        charset:  'utf8'
    },
    useNullAsDefault: true
})

var bookshelf = require('bookshelf')(knex)

bookshelf.plugin('registry')

module.exports = {
    knex:      knex,
    bookshelf: bookshelf
}
