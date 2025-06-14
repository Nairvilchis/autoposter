import React, { memo } from 'react';
import { Handle, Position } from 'react-flow-renderer';

const ExecuteJavascriptNode = ({ data }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: 10, borderRadius: 5, background: '#fff' }}>
      <div>
        <strong>Ejecutar Javascript</strong>
      </div>
      <div>
        <label htmlFor="javascript-input">Javascript:</label>
        <textarea id="javascript-input" defaultValue={data.script} />
      </div>
      <Handle type="target" position={Position.Top} id="a" />
      <Handle type="source" position={Position.Bottom} id="b" />
    </div>
  );
};

export default memo(ExecuteJavascriptNode);