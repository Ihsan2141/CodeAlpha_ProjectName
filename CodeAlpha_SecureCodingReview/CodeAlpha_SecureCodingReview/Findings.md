# Security Findings

## Finding 1: Hardcoded Credentials

Severity: High

Description:
The application contains hardcoded administrator credentials within the source code.

Risk:
Attackers who gain access to the source code can easily obtain valid credentials.

---

## Finding 2: SQL Injection Vulnerability

Severity: Critical

Description:
User input is directly concatenated into SQL queries without validation or parameterization.

Example Attack:

' OR '1'='1

Risk:
Attackers may bypass authentication, access sensitive data, or manipulate database contents.

---

## Finding 3: Cross-Site Scripting (XSS)

Severity: High

Description:
User-supplied comments are displayed without sanitization.

Example Payload:

<script>alert('XSS')</script>

Risk:
Attackers may execute malicious JavaScript, steal session tokens, or redirect users.

---

## Finding 4: Lack of Input Validation

Severity: Medium

Description:
All user inputs are accepted without validation.

Risk:
Increases exposure to injection and data manipulation attacks.

---

## Overall Risk Level

High
