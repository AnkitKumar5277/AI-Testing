# QA Agent Skills

A beginner-friendly Agent Skill project for diagnosing flaky tests.

## Project Goal

This project demonstrates how an AI agent can use a reusable
skill to investigate flaky automated tests.

## Structure

.claude/skills/flaky-triage/
    SKILL.md
    scripts/
    references/
    assets/

## Run the flaky test

pytest tests/test_login.py

## Run the test 20 times

python .claude/skills/flaky-triage/scripts/rerun_test.py tests/test_login.py

## Skill

The flaky-triage skill helps the AI:

1. Reproduce flaky tests
2. Measure failure rate
3. Compare isolated and suite execution
4. Classify failures
5. Identify root cause
6. Suggest the smallest fix

## Failure Categories

- Timing
- Ordering
- Shared Data
- Environment
- Product Bug

## Important Rule

Do not hide flaky tests using unnecessary retries.
Find and fix the root cause.

Others: 
                 AI AGENT
                    │
                    ▼
             Skill description
                    │
             "Is this relevant?"
                    │
             ┌──────┴──────┐
             │             │
            NO            YES
             │             │
             ▼             ▼
          Nothing       SKILL.md
                           │
                    ┌──────┴───────┐
                    │              │
                 scripts       references
                    │              │
                execute       read when needed