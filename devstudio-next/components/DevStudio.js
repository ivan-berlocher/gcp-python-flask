import dynamic from 'next/dynamic';
import { useEffect, useState } from 'react';
import FileTreePanel from './FileTreePanel';
import TestInputPanel from './TestInputPanel';
import LogsPanel from './LogsPanel';

const MonacoEditor = dynamic(() => import('./MonacoEditor'), { ssr: false });

export default function DevStudio() {
  const [tools, setTools] = useState([]);
  const [selectedTool, setSelectedTool] = useState(null);
  const [schema, setSchema] = useState(null);
  const [logs, setLogs] = useState('');

  useEffect(() => {
    fetch('/tools')
      .then(res => res.json())
      .then(data => setTools(data))
      .catch(err => setLogs(prev => prev + `\nError loading tools: ${err}`));
  }, []);

  useEffect(() => {
    if (!selectedTool) return;
    fetch(`/tools/${selectedTool.id}/schema`)
      .then(res => res.json())
      .then(setSchema)
      .catch(err =>
        setLogs(prev => prev + `\nError loading schema: ${err}`)
      );
  }, [selectedTool]);

  const runTool = async formData => {
    if (!selectedTool) return;
    try {
      const res = await fetch(selectedTool.endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const text = await res.text();
      setLogs(text);
    } catch (err) {
      setLogs(`Error: ${err}`);
    }
  };

  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <div style={{ flex: 1 }}>
        <FileTreePanel tools={tools} onSelect={setSelectedTool} />
      </div>
      <div style={{ flex: 2, display: 'flex', flexDirection: 'column' }}>
        <MonacoEditor />
        <TestInputPanel schema={schema} onRun={runTool} />
        <LogsPanel logs={logs} />
      </div>
    </div>
  );
}
