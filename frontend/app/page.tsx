
export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <main className="flex-1 flex justify-center items-center">
        <div className="flex flex-col items-center w-160">
          <h1 className="text-4xl font-bold">Resolver</h1>
          <h2 className="text-xl">On-brand marketing content creation for ecommerce</h2>

          <label className="mt-4">Website URL</label>
          <input type="url" className="border border-gray-300 rounded w-72 p-2 bg-foreground text-black" />
          <button className="mt-4 px-4 py-2 bg-[var(--button-color)] text-black rounded">Sign Up</button>    

        </div>
      </main>
      <footer className="flex justify-center items-center">
      </footer>
    </div>
  );
}
