/*
README — TiendaRopa Starter

Resumen rápido
- Stack: Vite + React + TailwindCSS + Framer Motion + Supabase (Auth + Storage + Postgres)
- Estética: minimal, suave, "liquid glass" (glassmorphism con backdrop-filter), botones dinámicos y micro-interacciones.
- Funcionalidades incluidas en el starter: búsqueda, filtros por talla y categoría, tarjetas de producto, registro/login (Supabase), subida básica de imágenes, perfil de usuario y ejemplo de esquema SQL para crear tablas en Supabase.

Archivos incluidos en este documento (cópialos a tu proyecto):
- package.json (dependencias mínimas)
- tailwind.config.cjs
- postcss.config.cjs
- src/main.jsx
- src/App.jsx
- src/lib/supabaseClient.js
- src/components/NavBar.jsx
- src/components/Auth.jsx
- src/components/ProductCard.jsx
- src/components/ProductList.jsx
- src/styles/index.css
- supabase_schema.sql


----- package.json (para referencia) -----
{
  "name": "tienda-ropa-starter",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@supabase/supabase-js": "^2.0.0",
    "framer-motion": "^10.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "autoprefixer": "^10.4.0",
    "postcss": "^8.4.0",
    "tailwindcss": "^3.0.0",
    "vite": "^5.0.0"
  }
}


----- tailwind.config.cjs -----
module.exports = {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}

----- postcss.config.cjs -----
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}


----- src/main.jsx -----
import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import './styles/index.css'

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)


----- src/lib/supabaseClient.js -----
import { createClient } from '@supabase/supabase-js'

// Usa variables de entorno (VITE_) para que Vite las exponga
const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY

export const supabase = createClient(supabaseUrl, supabaseAnonKey)


----- src/App.jsx -----
import React, { useEffect, useState } from 'react'
import NavBar from './components/NavBar'
import ProductList from './components/ProductList'
import Auth from './components/Auth'
import { supabase } from './lib/supabaseClient'

export default function App() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    const session = supabase.auth.getSession().then(r => r.data.session)
    // getSession returns a promise; listen to changes
    supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null)
    })
    // fetch current session
    supabase.auth.getSession().then(({ data }) => setUser(data.session?.user ?? null))
  }, [])

  return (
    <div className="min-h-screen bg-[radial-gradient(ellipse_at_top_left,_var(--tw-gradient-stops))] from-white/90 via-slate-50 to-slate-100">
      <NavBar user={user} />
      <main className="max-w-6xl mx-auto px-6 py-10">
        <section className="mb-8">
          <h1 className="text-4xl font-semibold mb-2">TiendaRopa</h1>
          <p className="text-slate-600">Minimal, suave y dinámico — prueba los filtros y el registro.</p>
        </section>

        <Auth supabase={supabase} user={user} />

        <ProductList supabase={supabase} />
      </main>
    </div>
  )
}


----- src/components/NavBar.jsx -----
import React from 'react'
import { motion } from 'framer-motion'

export default function NavBar({ user }) {
  return (
    <header className="backdrop-blur-sm bg-white/40 border-b border-white/50 sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-6">
          <div className="text-xl font-semibold">TiendaRopa</div>
          <div className="hidden md:block">
            <input placeholder="Buscar producto..." className="px-4 py-2 rounded-lg shadow-sm bg-white/60 backdrop-filter backdrop-blur-sm" />
          </div>
        </div>

        <div className="flex items-center gap-3">
          <motion.button whileHover={{ scale: 1.03 }} whileTap={{ scale: 0.97 }} className="px-4 py-2 rounded-lg border border-gray-200 bg-white/60">
            Filtros
          </motion.button>

          <motion.button whileHover={{ scale: 1.03 }} whileTap={{ scale: 0.97 }} className="px-4 py-2 rounded-lg shadow-sm bg-gradient-to-br from-white/70 to-white/40 backdrop-blur-md">
            Perfil
          </motion.button>
        </div>
      </div>
    </header>
  )
}


----- src/components/Auth.jsx -----
import React, { useState } from 'react'
import { supabase } from '../lib/supabaseClient'

// Componente simple para registro/login con email+password.
export default function Auth({ user }) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState('')

  async function signUp() {
    setLoading(true)
    setMessage('')
    const { data, error } = await supabase.auth.signUp({ email, password })
    setLoading(false)
    if (error) setMessage(error.message)
    else setMessage('Revisa tu correo para confirmar (si está activado).')
  }

  async function signIn() {
    setLoading(true)
    setMessage('')
    const { data, error } = await supabase.auth.signInWithPassword({ email, password })
    setLoading(false)
    if (error) setMessage(error.message)
    else setMessage('Has iniciado sesión correctamente.')
  }

  async function signOut() {
    await supabase.auth.signOut()
  }

  if (user) {
    return (
      <div className="mb-6 p-4 rounded-2xl bg-white/60 backdrop-blur-md border">
        <p>Sesión iniciada como <strong>{user.email}</strong></p>
        <button className="mt-3 px-4 py-2 rounded-lg" onClick={signOut}>Cerrar sesión</button>
      </div>
    )
  }

  return (
    <div className="mb-6 p-4 rounded-2xl bg-white/60 backdrop-blur-md border">
      <div className="flex gap-2">
        <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" className="px-3 py-2 rounded-md" />
        <input value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" type="password" className="px-3 py-2 rounded-md" />
      </div>
      <div className="flex gap-3 mt-3">
        <button onClick={signIn} className="px-4 py-2 rounded-lg">Entrar</button>
        <button onClick={signUp} className="px-4 py-2 rounded-lg">Registrarse</button>
      </div>
      {loading && <p className="mt-2 text-sm">Cargando...</p>}
      {message && <p className="mt-2 text-sm">{message}</p>}
    </div>
  )
}


----- src/components/ProductCard.jsx -----
import React from 'react'
import { motion } from 'framer-motion'

export default function ProductCard({ product }) {
  return (
    <motion.article whileHover={{ translateY: -6 }} className="rounded-2xl overflow-hidden shadow-md bg-white/70 backdrop-blur-md border">
      <div className="aspect-[4/3] w-full bg-slate-100">
        {product.image_url ? (
          <img src={product.image_url} alt={product.name} className="w-full h-full object-cover" />
        ) : (
          <div className="w-full h-full flex items-center justify-center text-slate-400">Sin imagen</div>
        )}
      </div>
      <div className="p-4">
        <h3 className="font-medium">{product.name}</h3>
        <p className="text-sm text-slate-600">{product.category} · {product.sizes?.join(', ')}</p>
        <div className="mt-3 flex items-center justify-between">
          <div className="text-lg font-semibold">€{product.price}</div>
          <button className="px-3 py-1 rounded-md bg-white/60">Añadir</button>
        </div>
      </div>
    </motion.article>
  )
}


----- src/components/ProductList.jsx -----
import React, { useEffect, useState } from 'react'
import ProductCard from './ProductCard'

export default function ProductList({ supabase }) {
  const [products, setProducts] = useState([])
  const [query, setQuery] = useState('')
  const [sizeFilter, setSizeFilter] = useState('')

  useEffect(() => {
    fetchProducts()
  }, [])

  async function fetchProducts() {
    // ejemplo simple: trae todas las filas de 'products'
    const { data, error } = await supabase.from('products').select('*').order('created_at', { ascending: false })
    if (!error) setProducts(data ?? [])
  }

  const filtered = products.filter(p => {
    const q = query.toLowerCase()
    const matchesQ = !q || p.name.toLowerCase().includes(q) || p.category?.toLowerCase().includes(q)
    const matchesSize = !sizeFilter || (p.sizes || []).includes(sizeFilter)
    return matchesQ && matchesSize
  })

  return (
    <section>
      <div className="mb-4 flex items-center gap-3">
        <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Buscar..." className="px-3 py-2 rounded-md" />
        <select value={sizeFilter} onChange={e => setSizeFilter(e.target.value)} className="px-3 py-2 rounded-md">
          <option value="">Todas las tallas</option>
          <option value="XS">XS</option>
          <option value="S">S</option>
          <option value="M">M</option>
          <option value="L">L</option>
          <option value="XL">XL</option>
        </select>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {filtered.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </section>
  )
}


----- src/styles/index.css -----
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --glass-bg: rgba(255,255,255,0.55);
}

body {
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
}

/* efecto "liquid glass" simple */
.backdrop-blur-md {
  backdrop-filter: blur(8px) saturate(120%);
}

/* pequeñas mejoras visuales */
input, select, button {
  outline: none;
}


----- supabase_schema.sql -----
-- Ejecuta esto en la pestaña SQL del dashboard de Supabase o en tu migración

-- Tabla de productos
create table if not exists products (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  description text,
  price numeric(10,2) not null default 0,
  sizes text[],
  category text,
  image_url text,
  created_at timestamptz default now()
);

-- Tabla de perfiles (relacionada con auth.users)
create table if not exists profiles (
  id uuid references auth.users on delete cascade primary key,
  full_name text,
  phone text,
  created_at timestamptz default now()
);

-- Crea un bucket de storage llamado 'product-images' en Supabase para subir imágenes.


/*
NOTAS IMPORTANTES (leer):
- Crea un proyecto en supabase.com y copia la URL y la ANON KEY en un archivo .env:
  VITE_SUPABASE_URL=https://...supabase.co
  VITE_SUPABASE_ANON_KEY=ey...

- En Supabase: Auth -> Settings -> Email -> habilita/deshabilita confirmación de email según quieras.
- Para imágenes: Storage -> Create bucket 'product-images' (público o privado según política) y usa supabase.storage.from('product-images').upload(...) desde el frontend o mediante funciones server-side.
- Para producción: añade Row Level Security (RLS) y policies apropiadas para que solo usuarios autorizados puedan crear/editar productos.
- Para desplegar: Vercel es una opción muy sencilla con integración a repositorios Git (recomendado para Next.js). Si usas Vite, también puedes desplegar en Netlify o Vercel.

*/
