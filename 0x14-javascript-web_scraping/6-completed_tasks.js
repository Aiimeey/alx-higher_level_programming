#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    process.exit(1);
  }

  const todos = JSON.parse(body);

  const completedTasksByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});


/*
  const data = JSON.parse(body);

  const y = data.filter(x =>
    x.completed === true);

  const dic = {};
  y.forEach(x => {
  // if(dic.hasOwnProperty(x.userId)){
    if (dic[x.userId]) {
      dic[x.userId]++;
    } else {
      dic[x.userId] = 1;
    }
  });
  console.log(dic);
*/
