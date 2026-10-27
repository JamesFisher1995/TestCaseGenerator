# Roles and permissions

The service has **no login and no user roles**. All users are anonymous members of the public with identical access.

Permission/role test cases are **not applicable**. Instead consider:
- First-time visitor (cookie banner shown) vs returning visitor (cookie choice remembered)
- Analytics cookies accepted vs rejected
- JavaScript enabled vs disabled (the pollutant and local authority pickers use JS autocomplete; there are `_nojs` download routes)
- Desktop vs mobile viewport; keyboard-only and screen reader users (GOV.UK accessibility standards, WCAG 2.2 AA)
