import subprocess
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("python rerun_test.py <pytest-test-path> [runs]")
        sys.exit(1)

    test_path = sys.argv[1]

    runs = 20

    if len(sys.argv) >= 3:
        runs = int(sys.argv[2])

    passed = 0
    failed = 0

    print(f"Running: {test_path}")
    print(f"Total runs: {runs}")
    print("-" * 50)

    for run_number in range(1, runs + 1):

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                test_path,
                "-q",
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            passed += 1
            status = "PASS"
        else:
            failed += 1
            status = "FAIL"

        print(f"Run {run_number:02d}: {status}")

    failure_rate = (failed / runs) * 100

    print("-" * 50)
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")
    print(f"Failure rate: {failure_rate:.2f}%")


if __name__ == "__main__":
    main()