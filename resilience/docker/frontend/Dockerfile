FROM node:18-alpine

# Set work directory
WORKDIR /app

# Copy package files
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy project
COPY frontend/ /app/

# Expose port
EXPOSE 3000

# Command to run (development)
CMD ["npm", "start"]

