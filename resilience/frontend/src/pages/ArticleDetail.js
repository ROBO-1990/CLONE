import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getArticle } from '../services/api';
import './ArticleDetail.css';

function ArticleDetail() {
  const { slug } = useParams();
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchArticle = async () => {
      try {
        const response = await getArticle(slug);
        setArticle(response.data);
      } catch (error) {
        console.error('Error fetching article:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchArticle();
  }, [slug]);

  if (loading) {
    return <div className="loading">Chargement...</div>;
  }

  if (!article) {
    return (
      <div className="article-detail">
        <div className="container">
          <div className="error">Article non trouvé</div>
        </div>
      </div>
    );
  }

  return (
    <div className="article-detail">
      <div className="container">
        <Link to="/articles" className="back-link">← Retour aux articles</Link>
        <article>
          <h1>{article.title}</h1>
          {article.subtitle && <p className="subtitle">{article.subtitle}</p>}
          {article.featured_image && (
            <img src={article.featured_image} alt={article.title} className="featured-image" />
          )}
          {article.featured_image_url && (
            <img src={article.featured_image_url} alt={article.title} className="featured-image" />
          )}
          <div className="content" dangerouslySetInnerHTML={{ __html: article.content }} />
          {article.tags && article.tags.length > 0 && (
            <div className="tags">
              {article.tags.map((tag, index) => (
                <span key={index} className="tag">{tag.name || tag}</span>
              ))}
            </div>
          )}
          <div className="meta">
            {article.author && (
              <span>Par {article.author_name || article.author.username || article.author}</span>
            )}
            <span>
              {new Date(article.published_at || article.created_at).toLocaleDateString('fr-FR', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
              })}
            </span>
            {article.category && (
              <span>Catégorie: {article.category_name || article.category}</span>
            )}
          </div>
        </article>
      </div>
    </div>
  );
}

export default ArticleDetail;

