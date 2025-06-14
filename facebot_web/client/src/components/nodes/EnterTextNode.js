import React, { memo } from 'react';
import { Handle, Position } from 'react-flow-renderer';

const EnterTextNode = ({ data }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: 10, borderRadius: 5, background: '#fff' }}>
      <div>
        <strong>Ingresar Texto</strong>
      </div>
      <div>
        <label htmlFor="text-input">Texto:</label>
        <input id="text-input" type="text" defaultValue={data.text} />
      </div>
      <div>
        <label htmlFor="clear-checkbox">Limpiar antes:</label>
        <input id="clear-checkbox" type="checkbox" defaultChecked={data.clear} />
      </div>
      <Handle type="target" position={Position.Top} id="a" />
      <Handle type="source" position={Position.Bottom} id="b" />
    </div>
  );
};

export default memo(EnterTextNode);