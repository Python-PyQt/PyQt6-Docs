.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: 6177f1fe5a0d18456bcc32a8c430e5e1

A URL of this type has no authority component at all. Everything after scheme name and separator character (:) will be preserved as is without validation or canonicalization. All URLs of such a scheme will be considered as having the same origin (unless the ``NoAccessAllowed`` flag is used).
