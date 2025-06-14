import React, { memo } from 'react';
import { Handle, Position } from 'react-flow-renderer';

const ClickElementNode = ({ data }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: 10, borderRadius: 5, background: '#fff' }}>
      <div>
        <strong>Hacer Clic en Elemento</strong>
      </div>
      <Handle type="target" position={Position.Top} id="a" />
    </div>
  );
};


export default memo(ClickElementNode);