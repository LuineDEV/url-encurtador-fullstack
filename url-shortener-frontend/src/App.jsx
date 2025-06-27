import { useState } from 'react';
import './App.css';

function App() {
  const [longUrl, setLongUrl] = useState('');
  
  const [customShortCode, setCustomShortCode] = useState(''); 
  const [shortUrl, setShortUrl] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setShortUrl('');
    setError('');
    setIsLoading(true);

    // --- LÓGICA: PREPARA O CORPO DA REQUISIÇÃO ---

    const requestBody = {
      long_url: longUrl,
      
      // Inclui o short_code apenas se o usuário digitou algo
      ...(customShortCode && { short_code: customShortCode }),
    };

    try {
      const response = await fetch('http://localhost:8000/shorten', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      });

      const data = await response.json();

      if (!response.ok) {
        // Usa a mensagem de erro vinda da API se ela existir
        throw new Error(data.detail || 'Falha ao encurtar a URL.');
      }
      
      const fullShortUrl = `http://localhost:8000/${data.short_code}`;
      setShortUrl(fullShortUrl);

    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Encurtador de URL Profissional</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="url"
          placeholder="Cole sua URL longa aqui..."
          value={longUrl}
          onChange={(e) => setLongUrl(e.target.value)}
          required
        />
        {}
        <input
          type="text"
          placeholder="Apelido customizado (opcional)"
          value={customShortCode}
          onChange={(e) => setCustomShortCode(e.target.value)}
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Encurtando...' : 'Encurtar!'}
        </button>
      </form>

      {}
      {shortUrl && (
        <div className="result">
          <p>Sua URL curta está pronta!</p>
          <a href={shortUrl} target="_blank" rel="noopener noreferrer">
            {shortUrl}
          </a>
        </div>
      )}
      {error && (
        <div className="error">
          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default App;