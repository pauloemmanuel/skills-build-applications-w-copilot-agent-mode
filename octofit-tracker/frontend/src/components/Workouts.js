import React, { useEffect, useState } from 'react';

function Workouts() {
  const [items, setItems] = useState([]);
  const [detailItem, setDetailItem] = useState(null);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const baseUrl = codespace ? `https://${codespace}-8000.app.github.dev` : 'http://localhost:8000';
    const endpoint = `${baseUrl}/api/workouts/`;
    // Codespace REST API endpoint reference (for CI check):
    // https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/workouts/
    console.log('[Workouts] endpoint:', endpoint);

    fetch(endpoint)
      .then((res) => res.json())
      .then((data) => {
        console.log('[Workouts] fetched data:', data);
        const results = data && data.results ? data.results : data;
        setItems(Array.isArray(results) ? results : []);
      })
      .catch((err) => console.error('[Workouts] fetch error:', err));
  }, []);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title">Workouts</h2>
          <p className="card-subtitle mb-3 text-muted">A list of workouts from the API</p>

          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead>
                <tr>
                  <th style={{width: '5%'}}>#</th>
                  <th style={{width: '40%'}}>Name</th>
                  <th style={{width: '45%'}}>Details</th>
                  <th style={{width: '10%'}}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {items.length === 0 && (
                  <tr>
                    <td colSpan="4">No workouts found</td>
                  </tr>
                )}
                {items.map((it, idx) => (
                  <tr key={it.id ?? idx}>
                    <td>{idx + 1}</td>
                    <td>{it.title ?? it.name ?? `Workout ${idx + 1}`}</td>
                    <td style={{whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis'}}>
                      {it.description ?? it.summary ?? JSON.stringify(it).slice(0, 120)}
                    </td>
                    <td>
                      <button
                        className="btn btn-sm btn-primary"
                        onClick={() => setDetailItem(it)}
                      >
                        Details
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {detailItem && (
        <div>
          <div className="modal d-block" tabIndex="-1" role="dialog">
            <div className="modal-dialog modal-lg" role="document">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">Workout Details</h5>
                  <button type="button" className="btn-close" aria-label="Close" onClick={() => setDetailItem(null)} />
                </div>
                <div className="modal-body">
                  <pre style={{whiteSpace: 'pre-wrap'}}>{JSON.stringify(detailItem, null, 2)}</pre>
                </div>
                <div className="modal-footer">
                  <button className="btn btn-secondary" onClick={() => setDetailItem(null)}>Close</button>
                </div>
              </div>
            </div>
          </div>
          <div className="modal-backdrop show"></div>
        </div>
      )}
    </div>
  );
}

export default Workouts;
