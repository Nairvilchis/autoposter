import React, { memo, useCallback, useState, useEffect } from 'react';
import { Handle, Position } from 'react-flow-renderer';
import { navigate } from '../../api/seleniumApi'; // Import the navigate function

const NavigateNode = ({ id, data }) => {
  const [url, setUrl] = useState(data.url || ''); // Use local state for the URL

  const handleChange = (event) => {
    setUrl(event.target.value);
  };

  const handleBlur = useCallback(async () => {
    try {
      await navigate(url); // Call the navigate API when the input loses focus
    } catch (error) {
      console.error('Error al navegar:', error);
      // Handle error appropriately (e.g., display an error message)
    } finally {
        if (data.url !== url) {
          data.url = url;
        }
    }
  }, [url, data]);
  
  useEffect(() => {
    if (data.url !== url) {
      data.url = url;
    }
  }, [url, data]);

  return (
    <div style={{ border: '1px solid #ccc', padding: 10, borderRadius: 5, background: '#fff' }}>
      <div>
        <strong>Navegar a URL</strong>
      </div>
      <div>
        <label htmlFor="url-input">URL:</label>
        <input
          id="url-input"
          type="text"
          value={url} // Connect the input to the local state
          onChange={handleChange} // Update the state when the input changes
          onBlur={handleBlur} // Call the API when the input loses focus
        />
      </div>
      <Handle type="source" position={Position.Bottom} id="a" />
    </div>
  );
};

export default memo(NavigateNode);