FROM node:20

WORKDIR /app

# Copy only package.json and package-lock.json first
COPY package*.json ./

# Install dependencies
RUN npm install

# Now copy the rest of the app
COPY . .

# Start the app
CMD ["npm", "start"]