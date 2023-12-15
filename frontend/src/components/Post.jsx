// Post.jsx
import React, { useState } from 'react';
import axios from 'axios';

function Post() {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [result, setResult] = useState(null);

  const handleAddNumbers = async () => {
    try {
      const response = await axios.post('http://localhost:8000/add/', {
        num1,
        num2,
      });
      setResult(response.data.result);
    } catch (error) {
      console.error('Error adding numbers:', error);
    }
  };

  return (
    <div>
      <h1>Add Two Numbers</h1>
      <label>
        Number 1:
        <input type="number" value={num1} onChange={(e) => setNum1(e.target.value)} />
      </label>
      <br />
      <label>
        Number 2:
        <input type="number" value={num2} onChange={(e) => setNum2(e.target.value)} />
      </label>
      <br />
      <button onClick={handleAddNumbers}>Add Numbers</button>
      <br />
      {result !== null && <p>Result: {result}</p>}
    </div>
  );
}

export default Post;
