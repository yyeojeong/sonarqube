const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  let a = 1;
  let b = 2;
  let c = 1 + 2;
  console.log('1+2='+c);
  res.send('Hello World!');
});

let server;

const hello1 = (a, b) => {
  console.log('hello1', a, b);
  return a + ':' + b;
}

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