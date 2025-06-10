import dynamic from 'next/dynamic';
import { useState } from 'react';

const Editor = dynamic(
  () => import('@monaco-editor/react').then(mod => mod.default),
  { ssr: false }
);

export default function MonacoEditor() {
  const [code, setCode] = useState('// Write code here');
  return (
    <div style={{ flex: 1 }}>
      <Editor
        height="50vh"
        defaultLanguage="javascript"
        value={code}
        onChange={value => setCode(value)}
        options={{ minimap: { enabled: false } }}
      />
    </div>
  );
}
