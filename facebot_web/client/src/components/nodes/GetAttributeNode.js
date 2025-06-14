import React, { memo } from 'react';
import { Handle, Position } from 'react-flow-renderer';

const GetAttributeNode = ({ data }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: 10, borderRadius: 5, background: '#fff' }}>
      <div>
        <strong>Obtener Atributo de Elemento</strong>
      </div>
      <div>
        <label htmlFor="attribute-name-input">Nombre del Atributo:</label>
        <input id="attribute-name-input" type="text" defaultValue={data.attributeName} />
      </div>
      <Handle type="target" position={Position.Top} id="a" />
      <Handle type="source" position={Position.Bottom} id="b" />
    </div>
  );
};

export default memo(GetAttributeNode);