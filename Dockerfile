FROM python:3.8.5

#Variable in time build
ARG CODEARTIFACT_TOKEN

ARG CODEARTIFACT_URL

ARG DATABASENAME
ENV DATABASENAME=$DATABASENAME

ARG PASSWORD
ENV PASSWORD=$PASSWORD

ARG USERNAME
ENV USERNAME=$USERNAME

ARG PORT
ENV PORT=$PORT

ARG ENDPOINT
ENV ENDPOINT=$ENDPOINT

ARG KEYCLOAK_PUBLIC_KEY
ENV KEYCLOAK_PUBLIC_KEY=$KEYCLOAK_PUBLIC_KEY

ARG KEYCLOAK_SERVER_URL
ENV KEYCLOAK_SERVER_URL=$KEYCLOAK_SERVER_URL

ARG KEYCLOAK_REALM
ENV KEYCLOAK_REALM=$KEYCLOAK_REALM

ARG KEYCLOAK_CLIENT_ID
ENV KEYCLOAK_CLIENT_ID=$KEYCLOAK_CLIENT_ID

ARG KEYCLOAK_CLIENT_SECRET_KEY
ENV KEYCLOAK_CLIENT_SECRET_KEY=$KEYCLOAK_CLIENT_SECRET_KEY

ARG APP_URL_AUTHENTICATION
ENV APP_URL_AUTHENTICATION=$APP_URL_AUTHENTICATION

#Create directory
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy application
COPY . /app

#Configuring PIP
RUN pip config set global.index-url https://aws:${CODEARTIFACT_TOKEN}@${CODEARTIFACT_URL}

#Install requirements                 
RUN pip install --no-cache-dir -r /app/requirements.txt

#Create user
RUN useradd -m pythonuser

#Permission on directories
RUN chown -R pythonuser:pythonuser /app/ 

#select user
USER pythonuser 

#Collects static files
RUN python manage.py collectstatic --noinput

#Expose port of communication
EXPOSE 6008

# Run manage.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:6008"]