import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>Resilience Magazine</h3>
            <p>Gouvernance des risques et résilience. Informer, analyser, former et sensibiliser.</p>
          </div>
          <div className="footer-section">
            <h3>Navigation</h3>
            <ul>
              <li><Link to="/">Accueil</Link></li>
              <li><Link to="/articles">Actualités</Link></li>
              <li><Link to="/first-aid">Premiers Secours</Link></li>
              <li><Link to="/library">Bibliothèque</Link></li>
              <li><Link to="/about">À propos</Link></li>
              <li><Link to="/contact">Contact</Link></li>
            </ul>
          </div>
          <div className="footer-section">
            <h3>Ressources</h3>
            <ul>
              <li><Link to="/multimedia">Multimédia</Link></li>
              <li><Link to="/library">Ressources</Link></li>
              <li><Link to="/first-aid">Gestes qui sauvent</Link></li>
            </ul>
          </div>
          <div className="footer-section">
            <h3>Contact</h3>
            <ul>
              <li><Link to="/contact">Formulaire de contact</Link></li>
              <li><Link to="/about">Mentions légales</Link></li>
              <li><Link to="/about">Politique éditoriale</Link></li>
            </ul>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 Resilience Magazine. Tous droits réservés.</p>
          <p className="author-name">Mboro Alain Brillant</p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;

