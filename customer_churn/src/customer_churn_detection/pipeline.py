import logging
import time

from .decorators import timeit


logger = logging.getLogger(__name__)


class Pipeline:

    def __init__(self, steps):
        self._steps = steps

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
                step_name = step.__class__.__name__

                logger.info(
                    f"Step started: {step_name}",
                    extra={
                        "event": "step_start",
                        "records": len(data),
                    },
                )

                step_start = time.perf_counter()

                data = step.run(data)

                duration = time.perf_counter() - step_start

                logger.info(
                    f"Step completed: {step_name}",
                    extra={
                        "event": "step_end",
                        "records": len(data),
                        "duration": duration,
                    },
                )

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