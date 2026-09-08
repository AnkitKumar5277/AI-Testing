# Retry and Wait Patterns

## Rule 1 — Do not use retry as the first solution

A retry can hide the real problem.

Bad approach:

```python
for _ in range(3):
    try:
        run_test()
        break
    except:
        pass