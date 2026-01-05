import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Articles
export const getArticles = (params) => api.get('/articles/', { params });
export const getArticle = (slug) => api.get(`/articles/${slug}/`);
export const getFeaturedArticles = () => api.get('/articles/featured/');
export const getLatestArticles = () => api.get('/articles/latest/');

// Content
export const getDossiers = (params) => api.get('/content/dossiers/', { params });
export const getDossier = (slug) => api.get(`/content/dossiers/${slug}/`);
export const getFeaturedDossiers = () => api.get('/content/dossiers/featured/');

// First Aid
export const getFirstAidGuides = (params) => api.get('/first-aid/guides/', { params });
export const getFirstAidGuide = (id) => api.get(`/first-aid/guides/${id}/`);
export const getFirstAidVideos = (params) => api.get('/first-aid/videos/', { params });
export const getQuizzes = (params) => api.get('/first-aid/quiz/', { params });
export const getQuiz = (id) => api.get(`/first-aid/quiz/${id}/`);
export const submitQuiz = (id, answers) => api.post(`/first-aid/quiz/${id}/submit/`, { answers });
export const getBadges = () => api.get('/first-aid/badges/');

// Multimedia
export const getVideos = (params) => api.get('/multimedia/videos/', { params });
export const getPodcasts = (params) => api.get('/multimedia/podcasts/', { params });
export const getPhotos = (params) => api.get('/multimedia/photos/', { params });
export const getWebinars = (params) => api.get('/multimedia/webinars/', { params });

// Library
export const getResources = (params) => api.get('/library/resources/', { params });
export const getResource = (id) => api.get(`/library/resources/${id}/`);
export const downloadResource = (id) => api.get(`/library/resources/${id}/download/`, { responseType: 'blob' });

// Users & Auth
export const register = (data) => api.post('/users/auth/register/', data);
export const login = (data) => api.post('/users/auth/login/', data);
export const refreshToken = (refresh) => api.post('/users/auth/refresh/', { refresh });
export const getCurrentUser = () => api.get('/users/me/');
export const updateUser = (data) => api.patch('/users/me/', data);
export const getUserBadges = () => api.get('/users/me/badges/');
export const getSavedContent = () => api.get('/users/me/saved-content/');
export const saveContent = (data) => api.post('/users/me/saved-content/', data);

// Comments
export const getComments = (articleId) => api.get(`/users/comments/?article=${articleId}`);
export const createComment = (data) => api.post('/users/comments/', data);

// Contact
export const sendContactMessage = (data) => api.post('/contact/messages/', data);
export const submitReporterApplication = (data) => api.post('/contact/reporters/', data);
export const subscribeNewsletter = (data) => api.post('/contact/newsletter/subscribe/', data);

// Maps
export const getRiskZones = (params) => api.get('/maps/risk-zones/', { params });
export const getAlerts = (params) => api.get('/maps/alerts/', { params });
export const getActiveAlerts = () => api.get('/maps/alerts/active/');

// Search
export const search = (query) => api.get('/search/', { params: { q: query } });

export default api;

