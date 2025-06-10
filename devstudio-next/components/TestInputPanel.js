import { useState } from 'react';

export default function TestInputPanel({ schema, onRun }) {
  const [text, setText] = useState('');
  if (!schema) {
    return (
      <div style={{ padding: '1rem', borderTop: '1px solid #ccc' }}>
        <h3>Select a tool</h3>
      </div>
    );
  }

  const handleSubmit = e => {
    e.preventDefault();
    onRun({ text });
  };

  return (
    <div style={{ padding: '1rem', borderTop: '1px solid #ccc' }}>
      <h3>{schema.title}</h3>
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={e => setText(e.target.value)}
          rows={4}
          style={{ width: '100%' }}
        />
        <button type="submit">Run</button>
      </form>
    </div>
  );
}
