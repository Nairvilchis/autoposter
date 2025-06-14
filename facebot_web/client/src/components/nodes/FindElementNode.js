import React, { memo } from 'react';
import { Handle, Position } from 'react-flow-renderer';

const FindElementNode = ({ data }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: 10, borderRadius: 5, background: '#fff' }}>
      <div>
        <strong>Encontrar Elemento</strong>
      </div>
      <div>
        <label htmlFor="selector-input">Selector:</label>
        <input id="selector-input" type="text" defaultValue={data.selector} />
      </div>
      <div>
        <label htmlFor="selector-type-select">Tipo de Selector:</label>
        <select id="selector-type-select" defaultValue={data.selector_type}>
          <option value="CSS">CSS</option>
          <option value="XPATH">XPATH</option>
        </select>
      </div>
      <Handle type="target" position={Position.Top} id="a" />
      <Handle type="source" position={Position.Bottom} id="b" />
    </div>
  );
};

export default memo(FindElementNode);