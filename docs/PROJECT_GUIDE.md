# Project Guide

## Simple explanation
Password strength is about how difficult a password is to guess, not merely how many character types it contains. Length, unpredictability, pattern resistance, common-password checks, and context all matter.

## Technical explanation
Authentication verifies identity; authorization controls permissions. Passwords should be transformed with a slow password hashing/KDF before storage in a real authentication system. Salts make identical passwords produce different stored hashes and key-stretching increases attacker cost. MFA adds another authentication factor.

Credential stuffing is the reuse of previously exposed credential pairs against other services. Password reuse makes this attack more relevant.

## Entropy
A simple theoretical estimate is L x log2(N), where L is length and N is an estimated character pool. It assumes random selection, which human-generated passwords usually do not satisfy. Therefore this application combines the estimate with pattern analysis.

## Industry relevance
The project demonstrates authentication-security analysis, IAM concepts, application-security thinking, secure coding, privacy-aware API design, defensive security awareness, test automation, and secure random generation. These map to cybersecurity analyst, application security, IAM, security engineering, SOC, and secure software roles.

## Real-world controls
Password + MFA + secure password hashing + rate limiting/abuse protection + secure sessions + phishing protection + monitoring.

## Password vs passphrase
Long, unique passphrases composed of randomly selected words can be easier to remember and harder to guess. Avoid famous quotes and predictable phrases.

## Ten rules
1. Unique passwords. 2. Prefer longer passwords/passphrases. 3. Avoid personal information. 4. Avoid common passwords. 5. Avoid reuse. 6. Use a password manager. 7. Enable MFA. 8. Never share passwords. 9. Watch for phishing. 10. Change credentials when compromise is suspected/confirmed.
