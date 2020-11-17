const axios = require('axios');

const slackToken = 'xoxb-1509591762388-1509600568372-5jO2dSfswmbzLhxqmBU2hjwN';

run().catch(err => console.log(err));

async function run() {
  const url = 'https://slack.com/api/chat.postMessage';
  const res = await axios.post(url, {
    channel: '#test',
    text: 'Hi, Love YOU!'
  }, { headers: { authorization: `Bearer ${slackToken}` } });

  console.log('Done', res.data);
}