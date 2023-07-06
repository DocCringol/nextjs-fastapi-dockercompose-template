import axios from 'axios';

async function getData() {
  'use server'
  return JSON.stringify((await axios.get('http://backend:5000')).data);
}

export default async function Home() {
  const result = await getData()
  return (
    <div>
      {result}
    </div>
  );
}
