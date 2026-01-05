import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './FirstAid.css';

// Mock data pour les guides de premiers secours
const urgencyGuides = [
  {
    id: 1,
    type: 'flood',
    title: 'En cas d\'inondation',
    description: 'Guides pratiques pour se protéger et protéger les autres lors d\'inondations',
    image: 'https://images.unsplash.com/photo-1473580044384-7ba9967e16a0?w=800&h=500&fit=crop&q=80',
    checklist: [
      'Éviter les zones inondées',
      'Monter à l\'étage ou sur le toit',
      'Ne pas traverser les eaux en crue',
      'Écouter les alertes météo',
      'Avoir un kit d\'urgence prêt'
    ]
  },
  {
    id: 2,
    type: 'earthquake',
    title: 'En cas de séisme',
    description: 'Les réflexes à adopter avant, pendant et après un tremblement de terre',
    image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=500&fit=crop&q=80',
    checklist: [
      'S\'abriter sous une table solide',
      'S\'éloigner des fenêtres',
      'Rester calme et ne pas paniquer',
      'Après le séisme, vérifier les dégâts',
      'Écouter les instructions des autorités'
    ]
  },
  {
    id: 3,
    type: 'fire',
    title: 'En cas d\'incendie',
    description: 'Comment réagir face à un incendie et évacuer en toute sécurité',
    image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=500&fit=crop&q=80',
    checklist: [
      'Alerter les secours (18 ou 112)',
      'Évacuer immédiatement',
      'Rester près du sol (fumée monte)',
      'Fermer les portes derrière soi',
      'Ne jamais revenir en arrière'
    ]
  },
  {
    id: 4,
    type: 'landslide',
    title: 'En cas de glissement de terrain',
    description: 'Conduite à tenir face aux glissements de terrain',
    image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=500&fit=crop&q=80',
    checklist: [
      'Éviter les zones à risque',
      'Évacuer rapidement',
      'Ne pas s\'approcher des zones instables',
      'Suivre les consignes des autorités',
      'Rester informé des alertes'
    ]
  },
  {
    id: 5,
    type: 'storm',
    title: 'En cas de tempête / Vents violents',
    description: 'Protection contre les vents violents et les tempêtes',
    image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=500&fit=crop&q=80',
    checklist: [
      'Rester à l\'intérieur',
      'Éloigner les objets extérieurs',
      'Fermer portes et fenêtres',
      'Éviter les zones exposées',
      'Suivre les alertes météo'
    ]
  },
  {
    id: 6,
    type: 'heatwave',
    title: 'En cas de canicule',
    description: 'Comment se protéger lors des vagues de chaleur extrême',
    image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=500&fit=crop&q=80',
    checklist: [
      'Boire beaucoup d\'eau',
      'Rester à l\'ombre',
      'Éviter les activités physiques',
      'Rafraîchir son habitation',
      'Surveiller les personnes vulnérables'
    ]
  }
];

const firstAidVideos = [
  {
    id: 1,
    title: 'Position Latérale de Sécurité (PLS)',
    description: 'Apprenez à mettre une personne inconsciente en position latérale de sécurité',
    thumbnail: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&h=400&fit=crop&q=80',
    duration: '5:30'
  },
  {
    id: 2,
    title: 'Massage cardiaque et défibrillation',
    description: 'Les gestes essentiels de réanimation cardio-pulmonaire',
    thumbnail: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&h=400&fit=crop&q=80',
    duration: '8:15'
  },
  {
    id: 3,
    title: 'Arrêt d\'hémorragie',
    description: 'Comment stopper une hémorragie efficacement',
    thumbnail: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&h=400&fit=crop&q=80',
    duration: '4:20'
  },
  {
    id: 4,
    title: 'Gestion des brûlures',
    description: 'Premiers secours en cas de brûlure',
    thumbnail: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=600&h=400&fit=crop&q=80',
    duration: '6:10'
  }
];

function FirstAid() {
  const [selectedType, setSelectedType] = useState(null);

  return (
    <div className="first-aid-page">
      <div className="hero-section">
        <div className="container">
          <h1>Premiers Secours</h1>
          <p className="hero-subtitle">Formez-vous aux comportements sécuritaires et gestes salvateurs</p>
        </div>
      </div>

      <div className="container">
        <section className="guides-section">
          <h2 className="section-title">Prévention et conduite à tenir</h2>
          <p className="section-subtitle">Guides pratiques illustrés par type d'urgence</p>
          
          <div className="urgency-types">
            {urgencyGuides.map((guide) => (
              <div 
                key={guide.id} 
                className={`urgency-card ${selectedType === guide.type ? 'active' : ''}`}
                onClick={() => setSelectedType(selectedType === guide.type ? null : guide.type)}
              >
                <div className="urgency-image">
                  <img 
                    src={guide.image} 
                    alt={guide.title}
                    onError={(e) => {
                      e.target.src = 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=500&fit=crop&q=80';
                    }}
                  />
                </div>
                <div className="urgency-content">
                  <h3>{guide.title}</h3>
                  <p>{guide.description}</p>
                  {selectedType === guide.type && (
                    <div className="checklist">
                      <h4>Checklist :</h4>
                      <ul>
                        {guide.checklist.map((item, index) => (
                          <li key={index}>{item}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                  <button className="btn-guide">
                    {selectedType === guide.type ? 'Masquer' : 'Voir le guide complet'}
                  </button>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="videos-section">
          <h2 className="section-title">Vidéos tutoriels</h2>
          <p className="section-subtitle">Apprenez les gestes essentiels avec nos vidéos pédagogiques</p>
          
          <div className="videos-grid">
            {firstAidVideos.map((video) => (
              <div key={video.id} className="video-card">
                <div className="video-thumbnail">
                  <img src={video.thumbnail} alt={video.title} />
                  <div className="play-overlay">
                    <svg width="60" height="60" viewBox="0 0 60 60" fill="none">
                      <circle cx="30" cy="30" r="30" fill="white" fillOpacity="0.9"/>
                      <path d="M24 18L24 42L42 30L24 18Z" fill="var(--color-primary-dark)"/>
                    </svg>
                  </div>
                  <span className="video-duration">{video.duration}</span>
                </div>
                <div className="video-content">
                  <h3>{video.title}</h3>
                  <p>{video.description}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="download-section">
          <div className="download-box">
            <h2>Téléchargez nos guides</h2>
            <p>Affiches téléchargeables et check-lists pour votre kit d'urgence</p>
            <div className="download-buttons">
              <button className="btn-download">Guide complet PDF</button>
              <button className="btn-download">Affiches à imprimer</button>
              <button className="btn-download">Check-list kit d'urgence</button>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

export default FirstAid;
