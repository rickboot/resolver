'use client'

import { useState } from "react";

export default function Home() {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState<any | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
  
    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setResult({error: (err as Error).message || 'Unknown error'});
    }
    finally {
    setLoading(false);
  }
  }


  return (
    <div className="flex flex-col min-h-screen">
      <main className="flex-1 flex flex-col justify-center items-center">
        <div className="flex flex-col items-center w-160">
          <form onSubmit={handleSubmit} className="flex flex-col items-center">
            <h1 className="text-4xl font-bold">Resolver</h1>
            <h2 className="text-xl">On-brand Marketing Content Creation</h2>
            <label htmlFor="website-url" className="mt-4 text-black">Website URL</label>
            <input id="website-url" placeholder='https://example.com' type="url" className="border border-gray-300 rounded w-64 p-2 bg-foreground text-black text-center" onChange={(e) => setUrl(e.target.value)}/>
            <button disabled={loading || !url} className="disabled:opacity-50 mt-4 px-4 py-2 bg-[var(--button-color)] text-black rounded" type="submit">{loading ? 'Loading...' : 'Submit'}</button>    
          </form>
          {result && (
            <div className="mt-12 text-black w-96 text-center">
              <h2 className="font-bold text-lg">Brand Information</h2>
              <p className="mt-2" >{result.company_name}</p>
              <p className="mt-2">{result.website_url}</p>
              <p className="mt-2">{result.target_audience}</p>
              <p className="mt-2">{result.writing_style}</p>
              <p className="mt-2">{result.title}</p>
              <p className="mt-2">{result.description}</p>
              <p className="mt-2">{result.og_title}</p>
              <p className="mt-2">{result.og_description}</p>
              <p className="mt-2">{result.brand_colors.map((color: string) => color).join(", ")}</p>
            </div>
          )}
        </div>
      </main>
      <footer className="flex justify-center items-center">
      </footer>
    </div>
  );
}
