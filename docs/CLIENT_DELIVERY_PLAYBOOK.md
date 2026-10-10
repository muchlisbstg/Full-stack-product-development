# Client Delivery Playbook

A repeatable delivery path for custom web, mobile, backend, and automation projects. This playbook describes a working process, not a claim that every capability is already implemented in this repository.

## Delivery stages

| Stage | Required inputs | Deliverables | Exit gate |
|---|---|---|---|
| 1. Discover | Business goal, users, constraints, stakeholders | Brief, scope boundaries, success metrics, risks | Client confirms problem and desired outcome |
| 2. Specify | Approved brief, user feedback | PRD, user stories, acceptance criteria, non-functional requirements | Acceptance criteria are testable and prioritized |
| 3. Design | PRD, brand assets, content | User flows, wireframes, responsive UI, accessibility notes | Key flows reviewed; unresolved assumptions recorded |
| 4. Architect | Requirements, data sensitivity, scale | Context diagram, API contracts, data model, ADRs | Security, tenancy, backup, and failure modes reviewed |
| 5. Build | Approved design and architecture | Small reviewable changes, tests, docs | CI passes; no unresolved blocker findings |
| 6. Verify | Build candidate, acceptance criteria | Unit/integration/E2E evidence, accessibility and performance results | Acceptance criteria pass or exceptions are documented |
| 7. Release | Versioned artifact, rollback plan | Release notes, deployment checklist, monitoring plan | Human release approval and rollback readiness |
| 8. Handover | Accepted release, operating docs | Runbook, environment inventory, known limitations, training | Client confirms access and ownership transfer |

## Definition of ready

Before implementation starts, each work item should have:
- A unique identifier and clear user/business outcome.
- Scope and explicit exclusions.
- Testable acceptance criteria.
- Dependencies and a named owner.
- Security/privacy/data classification where relevant.
- A rollback or recovery consideration for changes that affect persisted data.

## Definition of done

- [ ] Acceptance criteria are verified with recorded evidence.
- [ ] Automated tests pass in CI.
- [ ] Secrets are not committed; configuration is documented in an example file.
- [ ] API errors, validation, authorization, and empty/loading states are considered.
- [ ] Accessibility and responsive behavior are checked for user-facing changes.
- [ ] Database changes include a migration and recovery notes.
- [ ] Observability includes actionable logs/metrics without secrets or unnecessary personal data.
- [ ] Documentation and known limitations are updated.
- [ ] Production-impacting actions have explicit human approval.

## Change control

1. Record the request and business reason.
2. Assess impact on scope, schedule, data, security, cost, and existing clients.
3. Update the PRD or acceptance criteria before implementation.
4. Create a small branch and pull request; avoid direct production changes.
5. Run required checks and obtain review.
6. Release only the reviewed commit and record the outcome.

## AI-assisted engineering boundary

AI can draft plans, tests, code, and review comments. A human remains accountable for validating output, approving changes, managing secrets, and authorizing production releases. AI-generated review signals are advisory and must never count as approval by themselves.

## Client handover checklist

- [ ] Repository and ownership transfer confirmed.
- [ ] Environment variables documented without exposing values.
- [ ] Deployment, rollback, backup, and restore steps tested or explicitly marked untested.
- [ ] Support contact, escalation path, and service expectations agreed.
- [ ] Third-party services, licensing, and recurring costs disclosed.
- [ ] Data retention, deletion, and access revocation process documented.
- [ ] Open defects, limitations, and deferred work accepted by the client.

## Suggested case-study format

For public portfolio material, use anonymized or authorized details only: **Problem → Constraints → Approach → Architecture → Evidence → Result → Lessons learned**. Never publish client secrets, personal data, private source code, or unverified business outcomes.
