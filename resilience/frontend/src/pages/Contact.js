import React, { useState } from 'react';
import './Contact.css';

function Contact() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
    type: 'general'
  });

  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Ici, vous pouvez ajouter l'appel API pour envoyer le formulaire
    console.log('Form submitted:', formData);
    setSubmitted(true);
    setTimeout(() => {
      setSubmitted(false);
      setFormData({
        name: '',
        email: '',
        subject: '',
        message: '',
        type: 'general'
      });
    }, 3000);
  };

  return (
    <div className="contact-page">
      <div className="hero-section">
        <div className="container">
          <h1>Contactez-nous</h1>
          <p className="hero-subtitle">Nous sommes là pour répondre à vos questions</p>
        </div>
      </div>

      <div className="container">
        <div className="contact-content">
          <div className="contact-info-section">
            <div className="info-card">
              <div className="info-icon">📧</div>
              <h3>Email</h3>
              <p>contact@resilience-magazine.org</p>
            </div>
            <div className="info-card">
              <div className="info-icon">📞</div>
              <h3>Téléphone</h3>
              <p>+33 1 23 45 67 89</p>
            </div>
            <div className="info-card">
              <div className="info-icon">📍</div>
              <h3>Adresse</h3>
              <p>123 Rue de la Résilience<br />75000 Paris, France</p>
            </div>
            <div className="info-card">
              <div className="info-icon">⏰</div>
              <h3>Horaires</h3>
              <p>Lundi - Vendredi<br />9h00 - 18h00</p>
            </div>
          </div>

          <div className="contact-form-section">
            <h2>Envoyez-nous un message</h2>
            {submitted ? (
              <div className="success-message">
                <p>✅ Votre message a été envoyé avec succès !</p>
              </div>
            ) : (
              <form className="contact-form" onSubmit={handleSubmit}>
                <div className="form-group">
                  <label htmlFor="type">Type de demande</label>
                  <select
                    id="type"
                    name="type"
                    value={formData.type}
                    onChange={handleChange}
                    required
                  >
                    <option value="general">Demande générale</option>
                    <option value="editorial">Support rédaction</option>
                    <option value="reporter">Candidature reporter</option>
                    <option value="partnership">Partenariat</option>
                    <option value="technical">Support technique</option>
                  </select>
                </div>

                <div className="form-group">
                  <label htmlFor="name">Nom complet</label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                    placeholder="Votre nom"
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="email">Email</label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    placeholder="votre.email@example.com"
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="subject">Sujet</label>
                  <input
                    type="text"
                    id="subject"
                    name="subject"
                    value={formData.subject}
                    onChange={handleChange}
                    required
                    placeholder="Objet de votre message"
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="message">Message</label>
                  <textarea
                    id="message"
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    required
                    rows="6"
                    placeholder="Votre message..."
                  />
                </div>

                <button type="submit" className="submit-btn">
                  Envoyer le message
                </button>
              </form>
            )}
          </div>
        </div>

        <section className="newsletter-section">
          <div className="newsletter-box">
            <h2>Abonnez-vous à notre newsletter</h2>
            <p>Recevez nos dernières actualités et alertes directement dans votre boîte mail</p>
            <form className="newsletter-form">
              <input
                type="email"
                placeholder="Votre adresse email"
                className="newsletter-input"
                required
              />
              <button type="submit" className="btn-primary">S'abonner</button>
            </form>
          </div>
        </section>

        <section className="reporter-section">
          <div className="reporter-box">
            <h2>Reporters du monde</h2>
            <p>
              Vous souhaitez rejoindre notre communauté de reporters du bout du monde ? 
              Téléchargez notre formulaire de candidature et envoyez-le nous.
            </p>
            <div className="reporter-actions">
              <button className="btn-download">Télécharger le formulaire</button>
              <p className="reporter-note">
                Formulaire disponible en format PDF. Remplissez-le et renvoyez-le à 
                reporters@resilience-magazine.org
              </p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

export default Contact;
