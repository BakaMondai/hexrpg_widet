const express = require('express')

function createServer() {

    const express = require('express')
    const app = express()
    const httpPort = 3000


    app.listen(httpPort, () => console.log(`App listening on port: ${httpPort}`))

    return app;
}

exports.server = function() {
    let server = createServer()
    return server
}

