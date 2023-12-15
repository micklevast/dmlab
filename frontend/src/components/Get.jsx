import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Get() {
  const [getData, setGetData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/my_get_view/');
        console.log(response.data);
        // Handle the data
        setGetData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []); // The empty dependency array ensures that this effect runs once when the component mounts

  return (
    <div>
      <h1>Get data from backend</h1>

      <h3>response data : {JSON.stringify(getData)}</h3>
      {/* Note: Displaying the object directly may not work, so use JSON.stringify to display the data */}
    </div>
  );
}

export default Get;
