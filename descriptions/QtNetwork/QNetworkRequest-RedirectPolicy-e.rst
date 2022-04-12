.. sip:enum-description::
    :status: todo
    :digest: 6310c997998d74c8163a9343e7003d4e

Indicates whether the Network Access API should automatically follow a HTTP redirect response or not.

**Note:** When Qt handles redirects it will, for legacy and compatibility reasons, issue the redirected request using GET when the server returns a 301 or 302 response, regardless of the original method used, unless it was HEAD.
