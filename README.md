# restjwt v.1

Simple REST API that runs on Heroku to handle JSON Web Tokens (JWTs) which
use the following algorithms:

+ HS256 - HMAC using SHA-256 hash algorithm (default)
+ HS384 - HMAC using SHA-384 hash algorithm
+ HS512 - HMAC using SHA-512 hash algorithm

It's a thin [Flask](https://github.com/mitsuhiko/flask) wrapper around [pyjwt](https://github.com/progrium/pyjwt).

## Demo

You can currently use the API at http://restjwt.herokuapp.com/

### Sample Token

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE`

### Secret
`bosco`

### Response

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE?secret=bosco

    {
      "project": "restjwt", 
      "projectUrl": "https://github.com/mcktrtl/restjwt"
    }

## What is JSON Web Token (JWT)?

This quote from resources below is more elegant than I could write it:

> JSON Web Token (JWT) is a compact URL-safe means of representing claims to be transferred between two parties. The claims in a JWT are encoded as a JSON object that is digitally signed using JSON Web Signature (JWS).


See these resources:

- http://jwt.io/
- https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-31
- http://www.intridea.com/blog/2013/11/7/json-web-token-the-useful-little-standard-you-haven-t-heard-about
- https://developer.atlassian.com/static/connect/docs/concepts/understanding-jwt.html

## What good is this?

My personal use-case was needing to decode and verify JWTs in a testing/debugging
environment where I couldn't easily decode JWTs myself or use a library,
but I could issue HTTP requests. Since it was a test/debugging environment,
security wasn't a concern. **Think twice before you use this code in a scenario
where you care about security.**

## Endpoints

### GET /:token?secret=:secret

Returns a JSON including claims **only if the signature is verified**. If you
want the claims regardless of whether it is verified, use `/<token>/eval` or
`/token/claims`.

If secret is not given, will default to an empty string.

#### Valid Response

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE?secret=bosco

    {
      "project": "restjwt", 
      "projectUrl": "https://github.com/mcktrtl/restjwt"
    }

#### Invalid Response

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE?secret=ovaltine

    {
      "message": "Signature verification failed", 
      "result": "error"
    }

### GET /:token/eval?secret=:secret

Returns a JSON including claims and a boolean value of whether verified.

If secret is not given, will default to an empty string.

#### Valid Response

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE/eval?secret=bosco

    {
      "claims": {
        "project": "restjwt", 
        "projectUrl": "https://github.com/mcktrtl/restjwt"
      }, 
      "signature": true
    }

#### Invalid Response

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE/eval?secret=ovaltine

    {
      "claims": {
        "project": "restjwt", 
        "projectUrl": "https://github.com/mcktrtl/restjwt"
      }, 
      "signature": false
    }

### GET /:token/verify?secret=:secret

Returns a 200 status code if verified. Returns 409 if not verified. **Does not return claims.**

If secret is not given, will default to an empty string. 

#### Valid Response

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE/verify?secret=bosco

Status Code 200

    {
      "result": "success"
    }

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE/verify?secret=ovaltine

#### Invalid Response

Status Code 409

    {
      "message": "Signature verification failed", 
      "result": "error"
    }


### GET /:token/claims

Returns a JSON with just the claims. **Does not verify signature.**

### Response

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE/claims

    {
      "project": "restjwt", 
      "projectUrl": "https://github.com/mcktrtl/restjwt"
    }

### GET /:token/header

Returns a JSON with just the header. **Does not verify signature.**

#### Response

http://restjwt.herokuapp.com/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoicmVzdGp3dCIsInByb2plY3RVcmwiOiJodHRwczovL2dpdGh1Yi5jb20vbWNrdHJ0bC9yZXN0and0In0.mBtfz91pdgOfkFLhnpB-leXmU-l3gDrAau5in3N8izE/header

    {
      "alg": "HS256", 
      "typ": "JWT"
    }

## Roadmap

- Tests
- A single POST decoding endpoint to use as an alternative of all the GET endpoints
- Permit selective verification of optional JWT claims such as:
  - iss (Issuer)
  - sub (Subject)
  - aud (Audience)
  - exp (Expiration Time)
  - nbf (Not Before)
- Encode JWTs (why not?)
  - Specify HS256/HS384/HS512