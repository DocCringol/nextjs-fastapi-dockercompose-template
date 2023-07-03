import './App.css';

import React, { useEffect, useState } from 'react';

function MyComponent() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://backend:5000')
      .then(response => {
        console.log(response);
        response.json()
      })
      .then(data => {
        console.log(data);
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      {data && <p>{data}</p>}
    </div>
  );
}


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <MyComponent />
      </header>
    </div>
  );
}

export default App;
