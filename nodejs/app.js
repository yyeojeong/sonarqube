const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

let server;

function startServer() {
  server = app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
  });
}

function stopServer(done) {
  if (server) {
    server.close(done);
  } else {
    done();
  }
}

if (require.main === module) {
  startServer();
}

module.exports = { app, startServer, stopServer };