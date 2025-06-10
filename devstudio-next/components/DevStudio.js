import dynamic from 'next/dynamic';
import FileTreePanel from './FileTreePanel';
import TestInputPanel from './TestInputPanel';
import LogsPanel from './LogsPanel';

const MonacoEditor = dynamic(() => import('./MonacoEditor'), { ssr: false });

export default function DevStudio() {
  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <div style={{ flex: 1 }}>
        <FileTreePanel />
      </div>
      <div style={{ flex: 2, display: 'flex', flexDirection: 'column' }}>
        <MonacoEditor />
        <TestInputPanel />
        <LogsPanel />
      </div>
    </div>
  );
}
