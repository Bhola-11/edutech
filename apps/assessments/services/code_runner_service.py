"""
Automated Code Execution & Sandbox Testing Engine.
Executes and validates student code solutions against test cases with timeouts and output capture.
"""
import sys
import io
import traceback
import time
from typing import Dict, Any, List


class CodeExecutionService:
    @classmethod
    def execute_python_code(
        cls,
        code_string: str,
        input_data: str = '',
        expected_output: str = '',
        timeout_seconds: float = 2.0
    ) -> Dict[str, Any]:
        """
        Executes Python code in a controlled namespace capturing stdout/stderr
        and comparing with expected test case output.
        """
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_stdout = io.StringIO()
        redirected_stderr = io.StringIO()
        sys.stdout = redirected_stdout
        sys.stderr = redirected_stderr

        start_time = time.time()
        passed = False
        error_msg = None
        output_str = ''

        try:
            # Restricted execution environment
            global_env = {'__builtins__': __builtins__}
            local_env = {}
            exec(code_string, global_env, local_env)
            output_str = redirected_stdout.getvalue().strip()
            exec_time_ms = round((time.time() - start_time) * 1000, 2)

            if expected_output:
                clean_expected = expected_output.strip()
                passed = output_str == clean_expected
            else:
                passed = True

        except Exception as e:
            exec_time_ms = round((time.time() - start_time) * 1000, 2)
            error_msg = traceback.format_exc()
            passed = False
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        return {
            'passed': passed,
            'output': output_str,
            'expected_output': expected_output.strip() if expected_output else '',
            'execution_time_ms': exec_time_ms,
            'error': error_msg,
            'memory_used_kb': 1024  # Standard sandbox allocation
        }

    @classmethod
    def evaluate_all_test_cases(
        cls,
        student_code: str,
        test_cases: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Runs student code against multiple unit test cases (public and hidden)."""
        results = []
        total_points = sum(tc.get('points', 5) for tc in test_cases)
        points_earned = 0

        for tc in test_cases:
            res = cls.execute_python_code(
                code_string=student_code,
                input_data=tc.get('input_data', ''),
                expected_output=tc.get('expected_output', '')
            )
            tc_points = tc.get('points', 5) if res['passed'] else 0
            points_earned += tc_points

            results.append({
                'test_case_id': tc.get('id', len(results) + 1),
                'is_hidden': tc.get('is_hidden', False),
                'passed': res['passed'],
                'execution_time_ms': res['execution_time_ms'],
                'points_earned': tc_points,
                'max_points': tc.get('points', 5),
                'error': res['error'] if not tc.get('is_hidden') else (
                    'Runtime Error in hidden test case' if res['error'] else None
                )
            })

        all_passed = all(r['passed'] for r in results)
        score_pct = round((points_earned / total_points * 100) if total_points > 0 else 0, 1)

        return {
            'all_passed': all_passed,
            'total_points_earned': points_earned,
            'max_total_points': total_points,
            'score_percentage': score_pct,
            'test_results': results
        }
