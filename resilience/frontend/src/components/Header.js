import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Header.css';

function Header() {
  const [searchQuery, setSearchQuery] = useState('');
  const [logoError, setLogoError] = useState(false);
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/search?q=${encodeURIComponent(searchQuery)}`);
    }
  };

  return (
    <header className="header">
      <div className="header-container">
        <Link to="/" className="logo">
          {!logoError && (
            <img 
              src="/logo.jpg"
              alt="Resilience Magazine" 
              className="logo-img" 
              onError={() => { 
                setLogoError(true);
              }} 
            />
          )}
          <span className="logo-text">Resilience Magazine</span>
        </Link>
        
        <nav className="nav">
          <Link to="/">Accueil</Link>
          <Link to="/articles">Actualités</Link>
          <Link to="/first-aid">Premiers Secours</Link>
          <Link to="/library">Bibliothèque</Link>
          <Link to="/about">À propos</Link>
          <Link to="/contact">Contact</Link>
        </nav>

        <div className="header-actions">
          <form onSubmit={handleSearch} className="search-box">
            <input
              type="text"
              placeholder="Rechercher..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="search-input"
            />
          </form>
          <Link to="/first-aid" className="btn-urgent">
            Urgence : Gestes qui sauvent
          </Link>
        </div>
      </div>
    </header>
  );
}

export default Header;

