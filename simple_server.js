const http = require('http')
let requestCount = 0
const server = http.createServer((request,response) => {
    requestCount++
    switch (request.url) {
        case '/students':
            response.write("STUDENTS")
            break;
        case '/courses':
            response.write("FRONT + BACK")
            break;
        default:
            response.write("404 not found")
    }
    response.write(" Team Euler: "+ requestCount)
    response.end()
})

server.listen(3003)

"http://localhost:3003/"
