import logging
import time

from .decorators import timeit
from .steps.base import Step


logger = logging.getLogger(__name__)


class Pipeline:

    def __init__(self, steps: list[Step]):
        self._steps = steps

    def _run_step(self, step: Step, data):
        step_name = step.__class__.__name__

        logger.info(
            f"Step started: {step_name}",
            extra={
                "event": "step_start",
                "records": len(data),
            },
        )

        start_time = time.perf_counter()

        result = step.run(data)

        duration = time.perf_counter() - start_time

        logger.info(
            f"Step completed: {step_name}",
            extra={
                "event": "step_end",
                "records": len(result),
                "duration": duration,
            },
        )

        return result

    @timeit
    def run(self, data):
        start_time = time.perf_counter()

        logger.info(
            "Pipeline started",
            extra={
                "event": "pipeline_start",
                "records": len(data),
            },
        )

        try:
            for step in self._steps:
                data = self._run_step(step, data)

            duration = time.perf_counter() - start_time

            logger.info(
                "Pipeline completed",
                extra={
                    "event": "pipeline_end",
                    "records": len(data),
                    "duration": duration,
                },
            )

            return data

        except Exception:
            logger.exception(
                "Pipeline failed",
                extra={
                    "event": "pipeline_error",
                },
            )
            raise