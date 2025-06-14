import React, { useState, useCallback } from 'react';
import ReactFlow, {
  addEdge,
  useNodesState,
  useEdgesState,
  Controls,
  Background,
} from 'react-flow-renderer';

import NavigateNode from './nodes/NavigateNode';
import FindElementNode from './nodes/FindElementNode';
import ClickElementNode from './nodes/ClickElementNode';
import EnterTextNode from './nodes/EnterTextNode';
import GetTextNode from './nodes/GetTextNode';
import GetAttributeNode from './nodes/GetAttributeNode';
import ExecuteJavascriptNode from './nodes/ExecuteJavascriptNode';
import UploadFileNode from './nodes/UploadFileNode'; // Importa el componente UploadFileNode

const initialNodes = [
  { key: '1', id: '1', type: 'navigate', data: { url: 'https://www.google.com' }, position: { x: 250, y: 5 } },
  { key: '2', id: '2', type: 'find_element', data: { selector: '', selector_type: 'CSS' }, position: { x: 250, y: 150 } },
  { key: '3', id: '3', type: 'click_element', position: { x: 250, y: 300 } },
  { key: '4', id: '4', type: 'enter_text', data: { text: '', clear: true }, position: { x: 250, y: 450 } },
  { key: '5', id: '5', type: 'get_text', data: {}, position: { x: 250, y: 600 } },
  { key: '6', id: '6', type: 'get_attribute', data: { attributeName: '' }, position: { x: 250, y: 750 } },
  { key: '7', id: '7', type: 'execute_javascript', data: { script: '' }, position: { x: 250, y: 900 } },
  { key: '8', id: '8', type: 'upload_file', data: { filePath: '' }, position: { x: 250, y: 1050 } }, // Añade un nodo UploadFileNode
];

const initialEdges = [
  { id: 'e1-2', source: '1', target: '2', sourceHandle: 'a', targetHandle: 'a' },
  { id: 'e2-3', source: '2', target: '3', sourceHandle: 'b', targetHandle: 'a' },
  { id: 'e3-4', source: '2', target: '4', sourceHandle: 'b', targetHandle: 'a' },
  { id: 'e4-5', source: '2', target: '5', sourceHandle: 'b', targetHandle: 'a' },
  { id: 'e5-6', source: '2', target: '6', sourceHandle: 'b', targetHandle: 'a' },
  { id: 'e6-7', source: '2', target: '7', sourceHandle: 'b', targetHandle: 'a' },
  { id: 'e7-8', source: '2', target: '8', sourceHandle: 'b', targetHandle: 'a' }, // Conecta los nodos
];

// Define los tipos de nodos personalizados
const nodeTypes = {
  navigate: NavigateNode,
  find_element: FindElementNode,
  click_element: ClickElementNode,
  enter_text: EnterTextNode,
  get_text: GetTextNode,
  get_attribute: GetAttributeNode,
  execute_javascript: ExecuteJavascriptNode,
  upload_file: UploadFileNode, // Añade el tipo de nodo 'upload_file'
};

const Flow = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback((params) => setEdges((eds) => addEdge(params, eds)), [setEdges]);

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      nodeTypes={nodeTypes}
      fitView
    >
      <Controls />
      <Background color="#aaa" gap={16} />
    </ReactFlow>
  );
};

export default Flow;