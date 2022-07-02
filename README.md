# Mars Site
This repo contains the code to run the site for Mars scores. This comprises
three main components:

1. Backend - DynamoDB based
2. Middleware - API Based (FastAPI for dev, Lambdas for Prod)
3. UI - Angular

The primary design principals I have in mind are:

1. Provide clean delineation and interfaces for components
2. Make deployment scripted (ie CI/CD patterns)
3. Leverage git for source control
