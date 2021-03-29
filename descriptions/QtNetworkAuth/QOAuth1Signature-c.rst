.. sip:class-description::
    :status: todo
    :brief: Implements OAuth 1 signature methods
    :digest: f679ff349461b5d7980e41b2dfb40de5

Implements OAuth 1 signature methods.

OAuth-authenticated requests can have two sets of credentials: those passed via the "oauth_consumer_key" parameter and those in the "oauth_token" parameter. In order for the server to verify the authenticity of the request and prevent unauthorized access, the client needs to prove that it is the rightful owner of the credentials. This is accomplished using the shared-secret (or RSA key) part of each set of credentials.

OAuth specifies three methods for the client to establish its rightful ownership of the credentials: "HMAC-SHA1", "RSA-SHA1", and "PLAINTEXT". Each generates a "signature" with which the request is "signed"; the first two use a digest of the data signed in generating this, though the last does not. The "RSA-SHA1" method is not supported here; it would use an RSA key rather than the shared-secret associated with the client credentials.
