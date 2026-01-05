import React, { useState } from 'react';
import './Library.css';

// Mock data pour les ressources
const resources = [
  {
    id: 1,
    title: 'Rapport Sendai Framework 2024',
    description: 'Évaluation de la mise en œuvre du cadre de Sendai pour la réduction des risques de catastrophe',
    category: 'Rapport',
    type: 'PDF',
    size: '2.5 MB',
    image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&h=400&fit=crop&q=80',
    downloadUrl: '#'
  },
  {
    id: 2,
    title: 'Guide pratique de gestion des risques',
    description: 'Manuel complet pour les décideurs et acteurs de terrain sur la gestion des risques',
    category: 'Guide',
    type: 'PDF',
    size: '5.2 MB',
    image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=400&fit=crop&q=80',
    downloadUrl: '#'
  },
  {
    id: 3,
    title: 'Politiques nationales de prévention',
    description: 'Compilation des politiques nationales et internationales de prévention des catastrophes',
    category: 'Politique',
    type: 'PDF',
    size: '3.8 MB',
    image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=400&fit=crop&q=80',
    downloadUrl: '#'
  },
  {
    id: 4,
    title: 'Outils techniques d\'analyse des risques',
    description: 'Matrices d\'analyse, listes de contrôle et outils techniques pour l\'évaluation des risques',
    category: 'Outil',
    type: 'ZIP',
    size: '12.5 MB',
    image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=400&fit=crop&q=80',
    downloadUrl: '#'
  },
  {
    id: 5,
    title: 'Cartographies et données ouvertes',
    description: 'Cartes interactives et données open data sur les zones à risques',
    category: 'Données',
    type: 'ZIP',
    size: '45.2 MB',
    image: 'https://images.unsplash.com/photo-1524661135-423995f22d0b?w=600&h=400&fit=crop&q=80',
    downloadUrl: '#'
  },
  {
    id: 6,
    title: 'Articles scientifiques - Résilience',
    description: 'Collection d\'articles scientifiques sur la résilience communautaire et la gouvernance des risques',
    category: 'Article',
    type: 'PDF',
    size: '8.7 MB',
    image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&h=400&fit=crop&q=80',
    downloadUrl: '#'
  },
  {
    id: 7,
    title: 'Rapport Banque Mondiale - Financement des risques',
    description: 'Analyse des mécanismes de financement des risques et assurance catastrophe',
    category: 'Rapport',
    type: 'PDF',
    size: '4.1 MB',
    image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=400&fit=crop&q=80',
    downloadUrl: '#'
  },
  {
    id: 8,
    title: 'Guide ONU - Réduction des risques',
    description: 'Guide des Nations Unies sur la réduction des risques de catastrophe',
    category: 'Guide',
    type: 'PDF',
    size: '6.3 MB',
    image: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=400&fit=crop&q=80',
    downloadUrl: '#'
  }
];

const categories = ['Tous', 'Rapport', 'Guide', 'Politique', 'Outil', 'Données', 'Article'];

function Library() {
  const [selectedCategory, setSelectedCategory] = useState('Tous');

  const filteredResources = selectedCategory === 'Tous'
    ? resources
    : resources.filter(resource => resource.category === selectedCategory);

  return (
    <div className="library-page">
      <div className="hero-section">
        <div className="container">
          <h1>Bibliothèque & Ressources</h1>
          <p className="hero-subtitle">Documents utiles aux chercheurs, décideurs et acteurs de terrain</p>
        </div>
      </div>

      <div className="container">
        <div className="filter-section">
          <h3>Filtrer par catégorie</h3>
          <div className="filter-buttons">
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
        </div>

        <div className="resources-grid">
          {filteredResources.map((resource) => (
            <div key={resource.id} className="resource-card">
              <div className="resource-image">
                <img 
                  src={resource.image} 
                  alt={resource.title}
                  onError={(e) => {
                    e.target.src = 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&h=400&fit=crop&q=80';
                  }}
                />
                <span className="resource-category">{resource.category}</span>
              </div>
              <div className="resource-content">
                <h3>{resource.title}</h3>
                <p>{resource.description}</p>
                <div className="resource-meta">
                  <span className="resource-type">{resource.type}</span>
                  <span className="resource-size">{resource.size}</span>
                </div>
                <a href={resource.downloadUrl} className="download-btn">
                  Télécharger
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Library;
