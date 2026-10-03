# Interview Preparation

**Why isn't Password123! automatically strong?** Composition rules do not remove predictable common-word and number patterns.

**Why not store submitted passwords?** The analyzer does not need persistence; storage would create unnecessary secret-management and breach risk.

**Why not store hashes for analytics?** Hashes are unnecessary for aggregate analytics and can still create avoidable privacy/security risk.

**Why use `secrets`?** It is intended for security-sensitive random generation, unlike general-purpose `random`.

**What is entropy?** A measure of uncertainty; the simple L x log2(N) estimate assumes random selection.

**What is credential stuffing?** Trying previously exposed username/password pairs against other services.

**Authentication vs authorization?** Authentication establishes identity; authorization controls allowed actions.

**Why Argon2id?** It is a password hashing/KDF approach with configurable computational and memory cost, designed to make offline guessing more expensive than a fast general-purpose hash.

**Production improvements?** HTTPS, CSP/security headers, rate limiting, production WSGI server, secure sessions, secret-free logs, appropriate password hashing, monitoring, threat modeling, and stronger organizational policies.
