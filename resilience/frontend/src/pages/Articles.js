import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getArticles } from '../services/api';
import './Articles.css';

// Mock data pour les articles
const mockArticles = [
  {
    id: 1,
    slug: 'gouvernance-risques-climatiques',
    title: 'Gouvernance des risques climatiques : enjeux et perspectives',
    excerpt: 'Analyse approfondie des mécanismes de gouvernance des risques climatiques à l\'échelle internationale et nationale.',
    featured_image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=500&fit=crop&q=80',
    category: 'Gouvernance',
    published_at: '2024-12-15',
    article_type: 'analysis'
  },
  {
    id: 2,
    slug: 'resilience-communautaire-afrique',
    title: 'Résilience communautaire en Afrique : initiatives locales',
    excerpt: 'Découvrez comment les communautés africaines développent des stratégies de résilience face aux catastrophes naturelles.',
    featured_image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=500&fit=crop&q=80',
    category: 'Résilience',
    published_at: '2024-12-12',
    article_type: 'news'
  },
  {
    id: 3,
    slug: 'politiques-prevention-inondations',
    title: 'Politiques de prévention des inondations : leçons apprises',
    excerpt: 'Retour sur les politiques publiques de prévention des inondations et leurs résultats dans différents pays.',
    featured_image: 'https://images.unsplash.com/photo-1473580044384-7ba9967e16a0?w=800&h=500&fit=crop&q=80',
    category: 'Politiques publiques',
    published_at: '2024-12-10',
    article_type: 'analysis'
  },
  {
    id: 4,
    slug: 'technologies-gestion-risques',
    title: 'Innovations technologiques dans la gestion des risques',
    excerpt: 'Les nouvelles technologies au service de la prévention et de la gestion des catastrophes naturelles.',
    featured_image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=500&fit=crop&q=80',
    category: 'Innovation',
    published_at: '2024-12-08',
    article_type: 'news'
  },
  {
    id: 5,
    slug: 'adaptation-changement-climatique',
    title: 'Adaptation au changement climatique : stratégies d\'action',
    excerpt: 'Comment les pays s\'adaptent-ils au changement climatique ? Analyse des stratégies d\'adaptation mises en place.',
    featured_image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=500&fit=crop&q=80',
    category: 'Climat',
    published_at: '2024-12-05',
    article_type: 'analysis'
  },
  {
    id: 6,
    slug: 'crises-humanitaires-evolution',
    title: 'Évolution des crises humanitaires : tendances 2024',
    excerpt: 'Analyse des tendances des crises humanitaires en 2024 et perspectives pour 2025.',
    featured_image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=500&fit=crop&q=80',
    category: 'Crises humanitaires',
    published_at: '2024-12-03',
    article_type: 'news'
  },
  {
    id: 7,
    slug: 'financement-assurance-catastrophe',
    title: 'Financement des risques et assurance catastrophe',
    excerpt: 'Comment financer la gestion des risques ? Focus sur les mécanismes d\'assurance catastrophe.',
    featured_image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=500&fit=crop&q=80',
    category: 'Financement',
    published_at: '2024-12-01',
    article_type: 'analysis'
  },
  {
    id: 8,
    slug: 'urbanisme-resilient',
    title: 'Urbanisme résilient : construire pour l\'avenir',
    excerpt: 'Les principes de l\'urbanisme résilient et leur application dans les villes modernes.',
    featured_image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800&h=500&fit=crop&q=80',
    category: 'Urbanisme',
    published_at: '2024-11-28',
    article_type: 'chronicle'
  }
];

const categories = ['Tous', 'Gouvernance', 'Résilience', 'Politiques publiques', 'Innovation', 'Climat', 'Crises humanitaires', 'Financement', 'Urbanisme'];

function Articles() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState('Tous');

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await getArticles();
        const fetchedArticles = response.data?.results || response.data || [];
        // Utiliser les données de l'API si disponibles, sinon utiliser mock data
        setArticles(fetchedArticles.length > 0 ? fetchedArticles : mockArticles);
      } catch (error) {
        console.error('Error fetching articles:', error);
        // En cas d'erreur, utiliser mock data
        setArticles(mockArticles);
      } finally {
        setLoading(false);
      }
    };
    fetchArticles();
  }, []);

  const filteredArticles = selectedCategory === 'Tous' 
    ? articles 
    : articles.filter(article => article.category === selectedCategory);

  if (loading) {
    return <div className="loading">Chargement...</div>;
  }

  return (
    <div className="articles-page">
      <div className="hero-section">
        <div className="container">
          <h1>Actualités & Analyses</h1>
          <p className="hero-subtitle">L'information la plus récente sur les risques et la résilience</p>
        </div>
      </div>

      <div className="container">
        <div className="articles-filters">
          {categories.map(category => (
            <button
              key={category}
              className={`filter-btn ${selectedCategory === category ? 'active' : ''}`}
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </button>
          ))}
        </div>

        <div className="articles-grid">
          {filteredArticles.map((article) => (
            <Link key={article.id} to={`/articles/${article.slug}`} className="article-card">
              <div className="article-image">
                <img 
                  src={article.featured_image || article.featured_image_url || 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=500&fit=crop&q=80'} 
                  alt={article.title}
                  onError={(e) => {
                    e.target.src = 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=500&fit=crop&q=80';
                  }}
                />
                {article.category && (
                  <span className="article-category">{article.category}</span>
                )}
              </div>
              <div className="article-card-content">
                <h2>{article.title}</h2>
                <p>{article.excerpt || article.subtitle}</p>
                <div className="article-meta">
                  <span className="date">
                    {new Date(article.published_at || article.created_at || new Date()).toLocaleDateString('fr-FR', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric'
                    })}
                  </span>
                  <span className="read-more">Lire la suite →</span>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Articles;

