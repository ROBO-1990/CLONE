import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getFeaturedArticles, getLatestArticles } from '../services/api';
import './Home.css';

function Home() {
  const [featuredArticles, setFeaturedArticles] = useState([]);
  const [latestArticles, setLatestArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [featured, latest] = await Promise.all([
          getFeaturedArticles(),
          getLatestArticles(),
        ]);
        setFeaturedArticles(featured.data?.results || featured.data || []);
        setLatestArticles(latest.data?.results || latest.data || []);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) {
    return <div className="loading">Chargement...</div>;
  }

  return (
    <div className="home">
      <section className="hero">
        <div className="hero-background"></div>
        <div className="container">
          <h1>Resilience Magazine</h1>
          <p className="hero-subtitle">Gouvernance des risques et résilience</p>
          <p className="hero-description">
            Informer, analyser, former et sensibiliser pour renforcer la culture du risque et la résilience des communautés
          </p>
          <div className="hero-actions">
            <Link to="/first-aid" className="btn-primary">
              Gestes de premiers secours
            </Link>
            <Link to="/articles" className="btn-secondary">
              Découvrir les articles
            </Link>
          </div>
        </div>
      </section>

      <section className="visual-banner">
        <div className="container">
          <div className="banner-grid">
            <div className="banner-item">
              <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=80" alt="Catastrophes naturelles" />
              <div className="banner-overlay">
                <h3>Catastrophes naturelles</h3>
                <p>Comprendre et se préparer</p>
              </div>
            </div>
            <div className="banner-item">
              <img src="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&q=80" alt="Résilience communautaire" />
              <div className="banner-overlay">
                <h3>Résilience communautaire</h3>
                <p>Communautés unies</p>
              </div>
            </div>
            <div className="banner-item">
              <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80" alt="Gouvernance des risques" />
              <div className="banner-overlay">
                <h3>Gouvernance des risques</h3>
                <p>Stratégies et politiques</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="quick-access">
        <div className="container">
          <h2 className="section-title">Accès rapide</h2>
          <div className="quick-access-grid">
            <div className="quick-access-card urgent">
              <div className="quick-access-image">
                <img 
                  src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&h=400&fit=crop&q=80" 
                  alt="Premiers Secours"
                  onError={(e) => {
                    e.target.src = 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&h=400&fit=crop&q=80';
                  }}
                />
              </div>
              <div className="quick-access-content">
                <h3>Premiers Secours</h3>
                <p>Guides pratiques et gestes qui sauvent en cas d'urgence</p>
                <Link to="/first-aid" className="btn-primary">
                  Accéder
                </Link>
              </div>
            </div>
            <div className="quick-access-card">
              <div className="quick-access-image">
                <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80" alt="Dossier du mois" />
              </div>
              <div className="quick-access-content">
                <h3>Dossier du mois</h3>
                <p>Découvrez notre dossier spécial du mois sur la résilience</p>
                <Link to="/articles" className="btn-primary">
                  Découvrir
                </Link>
              </div>
            </div>
            <div className="quick-access-card resilience">
              <div className="quick-access-image">
                <img src="https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&q=80" alt="Bibliothèque" />
              </div>
              <div className="quick-access-content">
                <h3>Bibliothèque</h3>
                <p>Ressources, rapports et guides téléchargeables</p>
                <Link to="/library" className="btn-primary">
                  Explorer
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="stats-section">
        <div className="container">
          <div className="stats-grid">
            <div className="stat-item">
              <h3>100+</h3>
              <p>Articles publiés</p>
            </div>
            <div className="stat-item">
              <h3>50+</h3>
              <p>Guides de premiers secours</p>
            </div>
            <div className="stat-item">
              <h3>20+</h3>
              <p>Dossiers thématiques</p>
            </div>
            <div className="stat-item">
              <h3>24/7</h3>
              <p>Ressources disponibles</p>
            </div>
          </div>
        </div>
      </section>

      {featuredArticles.length > 0 && (
        <section className="featured">
          <div className="container">
            <h2 className="section-title">Articles en vedette</h2>
            <div className="articles-grid">
              {featuredArticles.slice(0, 6).map((article) => (
                <Link key={article.id} to={`/articles/${article.slug}`} className="article-card">
                  {article.featured_image && (
                    <img src={article.featured_image} alt={article.title} />
                  )}
                  <div className="article-card-content">
                    <h3>{article.title}</h3>
                    <p>{article.excerpt || article.subtitle}</p>
                    <div className="article-meta">
                      <span className="date">
                        {new Date(article.published_at || article.created_at).toLocaleDateString('fr-FR')}
                      </span>
                      {article.category && (
                        <span className="category">{article.category}</span>
                      )}
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}

      {latestArticles.length > 0 && (
        <section className="latest">
          <div className="container">
            <h2 className="section-title">Derniers articles</h2>
            <div className="articles-list">
              {latestArticles.slice(0, 5).map((article) => (
                <Link key={article.id} to={`/articles/${article.slug}`} className="article-item">
                  <h3>{article.title}</h3>
                  <p>{article.excerpt || article.subtitle}</p>
                  <span className="date">
                    {new Date(article.published_at || article.created_at).toLocaleDateString('fr-FR', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric'
                    })}
                  </span>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}

      <section className="video-section">
        <div className="container">
          <h2 className="section-title">Pourquoi la gouvernance des risques importe ?</h2>
          <div className="video-container">
            <div className="video-placeholder">
              <div className="play-button">
                <svg width="80" height="80" viewBox="0 0 80 80" fill="none">
                  <circle cx="40" cy="40" r="40" fill="white" fillOpacity="0.9"/>
                  <path d="M32 24L32 56L56 40L32 24Z" fill="var(--color-primary-dark)"/>
                </svg>
              </div>
              <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&q=80" alt="Vidéo introductive" />
              <p className="video-description">Découvrez l'importance de la gouvernance des risques dans notre société moderne</p>
            </div>
          </div>
        </div>
      </section>

      <section className="first-aid-tutorials">
        <div className="container">
          <h2 className="section-title">Tutoriels Premiers Secours</h2>
          <p className="section-subtitle">Apprenez les gestes essentiels qui sauvent</p>
          <div className="tutorials-grid">
            <div className="tutorial-card">
              <img 
                src="https://images.unsplash.com/photo-1473580044384-7ba9967e16a0?w=600&h=400&fit=crop&q=80" 
                alt="Inondation"
                onError={(e) => {
                  e.target.src = 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop&q=80';
                }}
              />
              <div className="tutorial-content">
                <h3>En cas d'inondation</h3>
                <p>Guides pratiques pour se protéger et protéger les autres lors d'inondations</p>
                <Link to="/first-aid" className="tutorial-link">Voir le guide →</Link>
              </div>
            </div>
            <div className="tutorial-card">
              <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop&q=80" alt="Séisme" />
              <div className="tutorial-content">
                <h3>En cas de séisme</h3>
                <p>Les réflexes à adopter avant, pendant et après un tremblement de terre</p>
                <Link to="/first-aid" className="tutorial-link">Voir le guide →</Link>
              </div>
            </div>
            <div className="tutorial-card">
              <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop&q=80" alt="Incendie" />
              <div className="tutorial-content">
                <h3>En cas d'incendie</h3>
                <p>Comment réagir face à un incendie et évacuer en toute sécurité</p>
                <Link to="/first-aid" className="tutorial-link">Voir le guide →</Link>
              </div>
            </div>
            <div className="tutorial-card">
              <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop&q=80" alt="Tempête" />
              <div className="tutorial-content">
                <h3>En cas de tempête</h3>
                <p>Protection contre les vents violents et les tempêtes</p>
                <Link to="/first-aid" className="tutorial-link">Voir le guide →</Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="map-section">
        <div className="container">
          <h2 className="section-title">Carte Interactive des Risques</h2>
          <p className="section-subtitle">Visualisez les zones à risques et les alertes en temps réel</p>
          <div className="map-container">
            <div className="map-placeholder">
              <img src="https://images.unsplash.com/photo-1524661135-423995f22d0b?w=1200&q=80" alt="Carte des risques" />
              <div className="map-overlay">
                <Link to="/maps" className="btn-primary">Explorer la carte interactive</Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="newsletter-section">
        <div className="container">
          <div className="newsletter-box">
            <div className="newsletter-content">
              <h2>Restez informé</h2>
              <p>Recevez nos dernières actualités et alertes directement dans votre boîte mail</p>
            </div>
            <form className="newsletter-form">
              <input type="email" placeholder="Votre adresse email" className="newsletter-input" />
              <button type="submit" className="btn-primary">S'abonner</button>
            </form>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;

