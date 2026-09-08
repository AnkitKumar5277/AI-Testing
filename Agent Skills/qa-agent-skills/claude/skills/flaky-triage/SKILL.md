---
name: flaky-triage
description: Diagnose and classify flaky tests. Use when a test
passes locally but fails in CI, fails intermittently, becomes
green after rerun, or someone asks to investigate a flaky test.
---

# Flaky Test Triage

When investigating a flaky test, follow this process.

## Step 1 — Reproduce

Run the test multiple times.

Use:

scripts/rerun_test.py

Do not manually repeat the test when the script can perform the
repetitive execution.

## Step 2 — Compare isolated and suite execution

Determine whether the test fails:

- when executed alone
- when executed as part of the full suite

If it fails only in the suite, investigate:

- test ordering
- shared state
- shared test data
- environment dependencies

## Step 3 — Identify the failure category

Classify the failure as one of:

1. timing
2. ordering
3. shared data
4. environment

Explain the evidence for the classification.

## Step 4 — Find the smallest fix

Prefer fixing the root cause.

Do not automatically suggest:

- retrying the test
- increasing timeouts

Only suggest a timeout change when the evidence shows that the
environment is genuinely slow.

## Step 5 — Product bug vs test bug

If the evidence indicates that the application itself is broken,
clearly identify it as a product bug instead of modifying the test.

## References

When proposing a retry or wait-related fix, read:

references/retry-patterns.md

Only read this reference when proposing a fix.