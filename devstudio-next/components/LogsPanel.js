
export default function LogsPanel({ logs }) {
  return (
    <div style={{ padding: '1rem', borderTop: '1px solid #ccc' }}>
      <h3>Logs</h3>
      <pre style={{ whiteSpace: 'pre-wrap' }}>{logs}</pre>

    </div>
  );
}
