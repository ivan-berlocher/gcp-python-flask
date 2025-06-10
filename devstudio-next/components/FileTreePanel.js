
export default function FileTreePanel({ tools, onSelect }) {
  return (
    <div style={{ padding: '1rem', borderRight: '1px solid #ccc' }}>
      <h3>Tools</h3>
      <ul>
        {tools.map(tool => (
          <li key={tool.id}>
            <button onClick={() => onSelect(tool)}>{tool.name}</button>
          </li>
        ))}
      </ul>

    </div>
  );
}
