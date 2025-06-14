import React, { memo } from 'react';
import { Handle, Position } from 'react-flow-renderer';

const UploadFileNode = ({ data }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: 10, borderRadius: 5, background: '#fff' }}>
      <div>
        <strong>Cargar Imagen/Video/Archivo</strong>
      </div>
      <div>
        <label htmlFor="file-path-input">Ruta del Archivo:</label>
        <input id="file-path-input" type="text" defaultValue={data.filePath} />
      </div>
      <Handle type="target" position={Position.Top} id="a" />
      <Handle type="source" position={Position.Bottom} id="b" />
    </div>
  );
};

export default memo(UploadFileNode);