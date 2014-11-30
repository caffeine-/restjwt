# restjwt

Simple REST API that runs on Heroku to handle JSON Web Tokens (JWTs) which
use the following algorithms:

+ HS256 - HMAC using SHA-256 hash algorithm (default)
+ HS384 - HMAC using SHA-384 hash algorithm
+ HS512 - HMAC using SHA-512 hash algorithm

It's a thin Flask wrapper around [pyjwt](https://github.com/progrium/pyjwt).

## Endpoints

### GET /:token?secret=:secret

If secret is not given, will default to an empty string.

Returns a JSON including claims **only if the signature is verified**. If you
want the claims regardless of whether it is verified, use `/<token>/eval`

### GET /:token/eval?secret=:secret

If secret is not given, will default to an empty string.

Returns a JSON including claims and a boolean value of whether verified.

### GET /:secret/verify?secret=:secret

If secret is not given, will default to an empty string.

Returns a 200 response if verified. Otherwise returns an error.

**Does not return claims**

### GET /:secret/claims

Returns a JSON with just the claims. DOES NOT VERIFY!

### GET /:secret/header

Returns a JSON with just the header. DOES NOT VERIFY!
