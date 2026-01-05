import React from 'react';
import './About.css';

const teamMembers = [
  {
    id: 1,
    name: 'Dr. Marie Dubois',
    role: 'Directrice éditoriale',
    bio: 'Expert en gouvernance des risques avec 15 ans d\'expérience',
    image: 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=400&h=400&fit=crop&q=80'
  },
  {
    id: 2,
    name: 'Prof. Jean Martin',
    role: 'Rédacteur en chef',
    bio: 'Spécialiste en résilience climatique et adaptation',
    image: 'https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=400&h=400&fit=crop&q=80'
  },
  {
    id: 3,
    name: 'Sophie Laurent',
    role: 'Responsable premiers secours',
    bio: 'Formatrice certifiée en gestes qui sauvent',
    image: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=400&h=400&fit=crop&q=80'
  },
  {
    id: 4,
    name: 'Pierre Moreau',
    role: 'Expert cartographie',
    bio: 'Spécialiste en systèmes d\'information géographique',
    image: 'https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=400&h=400&fit=crop&q=80'
  }
];

const partners = [
  { name: 'ONU', logo: 'https://via.placeholder.com/150x80?text=ONU' },
  { name: 'IFRC', logo: 'https://via.placeholder.com/150x80?text=IFRC' },
  { name: 'Banque Mondiale', logo: 'https://via.placeholder.com/150x80?text=BM' },
  { name: 'Université', logo: 'https://via.placeholder.com/150x80?text=UNIV' },
  { name: 'ONG Partenaire', logo: 'https://via.placeholder.com/150x80?text=ONG' }
];

function About() {
  return (
    <div className="about-page">
      <div className="hero-section">
        <div className="container">
          <h1>À propos de Resilience Magazine</h1>
          <p className="hero-subtitle">Renforcer la culture du risque et la résilience</p>
        </div>
      </div>

      <div className="container">
        <section className="about-section">
          <h2>Notre Vision</h2>
          <p>
            Resilience Magazine a pour vision de renforcer la culture du risque et la résilience 
            des communautés face aux catastrophes naturelles et aux crises. Nous croyons qu'une 
            information accessible, des formations pratiques et une gouvernance efficace des risques 
            sont essentielles pour construire des sociétés plus résilientes.
          </p>
        </section>

        <section className="about-section">
          <h2>Notre Mission</h2>
          <div className="mission-grid">
            <div className="mission-item">
              <div className="mission-icon">📰</div>
              <h3>Informer</h3>
              <p>Fournir une information fiable et à jour sur les risques et la résilience</p>
            </div>
            <div className="mission-item">
              <div className="mission-icon">🔍</div>
              <h3>Analyser</h3>
              <p>Décrypter les enjeux complexes de la gouvernance des risques</p>
            </div>
            <div className="mission-item">
              <div className="mission-icon">🎓</div>
              <h3>Former</h3>
              <p>Former le grand public aux gestes de premiers secours et comportements sécuritaires</p>
            </div>
            <div className="mission-item">
              <div className="mission-icon">💡</div>
              <h3>Sensibiliser</h3>
              <p>Raising awareness about risk management and resilience strategies</p>
            </div>
          </div>
        </section>

        <section className="about-section">
          <h2>Philosophie éditoriale</h2>
          <p>
            Notre approche éditoriale privilégie la rigueur scientifique, l'accessibilité et 
            l'action pratique. Nous nous appuyons sur des experts reconnus, des données vérifiées 
            et des retours d'expérience de terrain. Chaque contenu est conçu pour être à la fois 
            informatif et actionnable, permettant à nos lecteurs de mieux comprendre les risques 
            et d'agir en conséquence.
          </p>
        </section>

        <section className="about-section">
          <h2>Notre Équipe</h2>
          <p className="section-intro">
            Une équipe d'experts, de rédacteurs et de partenaires scientifiques dédiés à la mission 
            de Resilience Magazine.
          </p>
          <div className="team-grid">
            {teamMembers.map((member) => (
              <div key={member.id} className="team-member">
                <div className="member-image">
                  <img 
                    src={member.image} 
                    alt={member.name}
                    onError={(e) => {
                      e.target.src = 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=400&h=400&fit=crop&q=80';
                    }}
                  />
                </div>
                <h3>{member.name}</h3>
                <p className="member-role">{member.role}</p>
                <p className="member-bio">{member.bio}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="about-section">
          <h2>Nos Partenaires</h2>
          <p className="section-intro">
            Resilience Magazine travaille en collaboration avec des institutions publiques, 
            des ONG, des think tanks, des universités et des organisations internationales.
          </p>
          <div className="partners-grid">
            {partners.map((partner, index) => (
              <div key={index} className="partner-logo">
                <img src={partner.logo} alt={partner.name} />
                <p>{partner.name}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="about-section">
          <h2>Mentions légales</h2>
          <p>
            Resilience Magazine est une publication dédiée à la gouvernance des risques et à la résilience. 
            Tous les contenus sont vérifiés et approuvés par notre comité éditorial. Pour toute question 
            ou réclamation, veuillez nous contacter via notre formulaire de contact.
          </p>
        </section>
      </div>
    </div>
  );
}

export default About;
